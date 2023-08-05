import os
from time import time
from loguru import logger
from psutil import STATUS_ZOMBIE
from tomclient.clients.jws_client import JWSClient
from tomclient.pods.manager import PodManager
from tomclient.utility import (
    list_servable_workload,
    parse_servable_config,
    safe_get_cuda_visible_devices,
)

RESERVED_CONFIG = ["CUDA_VISIBLE_DEVICES"]

class TomClient(JWSClient):
    def __init__(self, host_url, num_cards) -> None:
        super().__init__(host_url)
        tom_temp_path = os.environ.get("TOM_TEMP_PATH", None)
        self.podmanager = PodManager(tcmpod_dir=tom_temp_path)
        self.num_cards = num_cards
        self.status = {
            k:{
                "worker_id": k,
                "ip_addr": "",
                "gpu_specs": "",
                "gpu_memory": "",
                "current_workload": {
                    "workload": "",
                    "mode": "",
                },
                "metrics": {}
        } for k in range(num_cards)}
    
    def join(self, 
            gpu_id: int,
            ip_addr:str, 
            gpu_spec: str, 
            gpu_memory: str, 
            working_dir: str
        ):
        self.status[gpu_id]["ip_addr"] = ip_addr
        self.status[gpu_id]["gpu_spec"] = gpu_spec
        self.status[gpu_id]["gpu_memory"] = gpu_memory
        self.working_dir = working_dir
        self.servable = list_servable_workload(working_dir)
        self.status[gpu_id]["worker_id"] = self._run(
            self._join_worker,
            kwargs={
                "ip_addr": ip_addr,
                "gpu_spec": gpu_spec,
                "gpu_memory": gpu_memory,
                "servable": self.servable,
            },
        )
    
    def update_serving_status(self):
        for gpu_id in range(self.num_cards):
            workload_repr = f"{self.status[gpu_id]['current_workload']['workload']}:{self.status[gpu_id]['current_workload']['mode']}"
            self._run(
                self._update_serving,
                kwargs={"worker_id": self.status[gpu_id]["worker_id"], "workload": workload_repr},
            )
            current_time = int(time())
            for metric in self.status[gpu_id]['metrics']:
                self._run(
                    self._send_status,
                    kwargs={
                        "current_time": current_time,
                        "metric": metric,
                        "value": self.status[gpu_id]['metrics'][metric],
                        "worker_id": self.status[gpu_id]["worker_id"],
                        "ip_addr": self.status[gpu_id]["ip_addr"],
                        "gpu_spec": self.status[gpu_id]["gpu_spec"],
                        "gpu_memory": self.status[gpu_id]["gpu_memory"],
                        "servable": self.servable,
                    },
                )
    
    def update_status(self, gpu_id, metric, value):
        self.status[gpu_id]['metrics'][metric] = value

    def bootstrap_workload(self):
        for gpu_id in range(self.num_cards):
            new_workload = self._run(
                self._get_new_workload,
                kwargs={"worker_id": self.status[gpu_id]["worker_id"]},
            )
            if new_workload and new_workload["workload"] != "" and new_workload!=self.status[gpu_id]['current_workload']:
                logger.info(f"New workload: {new_workload}")
                logger.debug(f"Current workload: {self.status[gpu_id]['current_workload']}")
                # start pod here
                self.start_worker_pod(
                    new_workload=new_workload,
                    gpu_id=gpu_id
                )

    def start_worker_pod(self, new_workload, gpu_id=0):
        working_dir = os.path.join(self.working_dir, new_workload["workload"])
        bootstrap_payload = new_workload["bootstrap_config"]
        try:
            tom_config = parse_servable_config(working_dir)
        except Exception as e:
            logger.error(f"Failed to parse TOM configuration file: {e}")
            return
        pod_name = (
            tom_config["workload"] + ":" + new_workload["mode"] + ":" + self.status[gpu_id]["worker_id"]
        )
        envs = {env["name"]: env["value"] for env in tom_config["spec"]["env"]}
        for add_env in bootstrap_payload:
            if add_env not in RESERVED_CONFIG:
                envs[add_env] = bootstrap_payload[add_env]
        pod = self.podmanager.get_pod(pod_name)
        if pod is not None:
            logger.warning(f"Pod {pod_name} already exists.")
            return
        mode_found = False
        pod_config = {}
        for mode_entry in tom_config["mode"]:
            if mode_entry["name"] == new_workload["mode"]:
                mode_found = True
                # prepare additional environment variables
                # - particularly we need to process CUDA_VISIBLE_DEVICES
                try:
                    cuda_visible_devices = safe_get_cuda_visible_devices(
                        tom_config=tom_config,
                        bootstrap_payload = bootstrap_payload,
                        mode_entry = mode_entry,
                        current_gpu_id=gpu_id,
                        total_gpu_count=self.num_cards,
                    )
                    envs['CUDA_VISIBLE_DEVICES'] = cuda_visible_devices
                    pod_config['mode_entry'] = mode_entry
                    pod_config['envs'] = envs
                except Exception as e:
                    logger.error(f"Failed to allocate CUDA_VISIBLE_DEVICES: {e}")
                    return
        if not mode_found:
            logger.error(f"Mode {new_workload['mode']} not found.")
            return
        
        # pod arranagement
        # first find pods on the occupied GPUs
        # and kill them, we only need to handle pods
        # started on the certain occupied GPUs & 
        # release their workload
        if "CUDA_VISIBLE_DEVICES" in pod_config['envs']:
            occupied_gpus = pod_config['envs']['CUDA_VISIBLE_DEVICES'].split(',')
            for gpu_id in occupied_gpus:
                gpu_id = int(gpu_id)
                existing_pods_on_gpu =[pod for pod in self.podmanager.get_pods() if pod.name.endswith(self.status[gpu_id]['worker_id'])]
                self.podmanager.kill(existing_pods_on_gpu)
                # this is probably not necessary in the current code - as it will be updated soon after new workload is loaded
                # but in future this might be reported to tcm in an async manner
                # so it is always good to raise an alarm
                self.status[gpu_id]['current_workload'] = {"workload": "", "mode": ""}
        
        # now we can start the new pod
        logger.info(f"Creating a new pod for workload: {pod_config}")
        # once started - this will be put into background and won't block the main thread
        working_dir = os.path.join(self.working_dir, new_workload["workload"])

        self.podmanager.run(
            f"cd {working_dir} && /bin/bash {pod_config['mode_entry']['entrypoint']}",
            name = pod_name,
            check=True,
            additional_env=pod_config['envs'],
        )
        # now propagate the workload to all the GPUs
        for gpu_id in occupied_gpus:
            self.status[int(gpu_id)]['current_workload'] = new_workload

    def check_pods(self):
        # check all pods
        # this should be run if a SIGKILL-like is received
        pods = self.podmanager.get_pods()
        for pod in pods:
            if pod.proc is None:
                # this means the pod process cannot be found
                # If it is a pod started by TOM, we are obliged to properly
                # clean it up once it is finished.

                # But if the process is not found, while the pod is there
                # it means the pod is not properly killed by TOM
                # most probably, due to some errors TOM is killed 
                # without having a chance to clean up the pods
                self.podmanager.clean_pod(pod)
            if pod.proc.status() == STATUS_ZOMBIE:
                logger.info(f"releasing pod: {pod.name}")
                # this means the child process is finished, or exited with error
                # we need to clean up the pod and release the current_workload
                if "CUDA_VISIBLE_DEVICES" in pod.env:
                    occupied_gpus = pod.env['CUDA_VISIBLE_DEVICES'].split(',')
                    for gpu_id in occupied_gpus:
                        self.status[int(gpu_id)]['current_workload'] = {"workload": "", "mode": ""}
                # self.podmanager.clean_pod(pod)
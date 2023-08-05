from loguru import logger
from tomclient.clients.tom_client import TomClient
from tomclient.states.globals import shared_states
from tomclient.gpuml.gpu_profiler import gpu_measure

def clock_update_status(tom_client, gpu_id):
    gpu_stats = gpu_measure()
    if gpu_stats is not None and 'gpu' in gpu_stats:
        gpu_stats = gpu_stats['gpu']
        for idx, stat in enumerate(gpu_stats):
            gpu_util = stat["utilization"]
            power_usage = stat["power_readings"]["power_draw"]
            available_memory = stat["fb_memory_usage"]["free"]
            used_memory = stat["fb_memory_usage"]["used"]
            
            tom_client.update_status(gpu_id=idx, metric="Available Memory", value=available_memory)
            tom_client.update_status(gpu_id=idx, metric="Used Memory", value=used_memory)
            tom_client.update_status(gpu_id=idx, metric="GPU Utilization", value=gpu_util)
            tom_client.update_status(gpu_id=idx, metric="Power Usage", value=power_usage)
            tom_client.update_serving_status()

def clock_watch(sc, tom_client: TomClient, ip_addr: str, gpu_id: str):
    clock_update_status(tom_client, gpu_id)
    tom_client.bootstrap_workload()
    tom_client.check_pods()
    sc.enter(10, 1, clock_watch, (sc, tom_client, ip_addr, gpu_id))

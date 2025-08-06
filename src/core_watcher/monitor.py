import gpustat
import psutil


def get_status() -> dict[str, float]:
    return {
        "cpu": psutil.cpu_percent(),
        "gpu": gpustat.GPUStatCollection.new_query().gpus[0].utilization,
        "vram": psutil.virtual_memory().percent,
    }

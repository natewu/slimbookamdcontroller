import pyamdgpuinfo

class GpuService:

    @staticmethod
    def exists_amd_gpus() -> bool:
        return GpuService.get_number_of_gpus() > 0

    @staticmethod
    def get_number_of_gpus() -> int:
        return pyamdgpuinfo.detect_gpus()

    @staticmethod
    def get_model(gpu_index: int) -> str:
        return pyamdgpuinfo.get_gpu(gpu_index).name

    @staticmethod
    def get_vram(gpu_index: int) -> str:
        vram_size = GpuService._get_vram_size(gpu_index)
        temp_size = GpuService._convert_bytes_to_gbytes(vram_size)
        unit = 'GB'

        if temp_size == 0:
            temp_size = GpuService._convert_bytes_to_mbytes(vram_size)
            unit = 'MB'

        return '{} {}'.format(temp_size, unit)

    @staticmethod
    def get_temp(gpu_index: int) -> str:
        return '{} ºC'.format(pyamdgpuinfo.get_gpu(gpu_index).query_temperature())

    @staticmethod
    def get_slot(gpu_index: int) -> str:
        return pyamdgpuinfo.get_gpu(gpu_index).pci_slot
    
    @staticmethod
    def _get_vram_size(gpu_index: int) -> str:
        return pyamdgpuinfo.get_gpu(gpu_index).memory_info['vram_size']

    @staticmethod
    def _convert_bytes_to_gbytes(vram_size):
        return round(float(vram_size)/1024.0**3)
    
    @staticmethod
    def _convert_bytes_to_mbytes(vram_size):
        return round(float(vram_size)/1024.0**2)

import psutil
from enum import Enum, IntEnum

Enu = Enum('toto', '3 4 5')

class InfoMemory(object):
    def __init__(self, *args):
        super(InfoMemory, self).__init__(*args)

    def virtual_memory(self):
        return psutil.virtual_memory()

    def swap_memory(self):
        return psutil.swap_memory()

    def __format(self,memory_info, memory_type, unit):

        for info, data in memory_info.items():
            memory_info[info] = self.__convert(data, unit)

    def __convert(self, data, unit):
        return data / unit




InfoMemoryInst = InfoMemory()

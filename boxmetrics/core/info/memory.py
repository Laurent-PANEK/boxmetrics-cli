import psutil
from .base import Info


class Memory(Info):
    def __init__(self, *args):
        super(Memory, self).__init__(*args)

    def virtual_memory(self):
        format_data = self._format(psutil.virtual_memory()._asdict())
        return format_data

    def swap_memory(self, unit=None):
        format_data = self._format(psutil.swap_memory()._asdict())
        return format_data

    def all(self):
        virtual = self.virtual_memory()
        swap = self.swap_memory()
        return dict(virtual=virtual, swap=swap)


MemoryInst = Memory()

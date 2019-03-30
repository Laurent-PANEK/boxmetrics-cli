import psutil


class InfoMemory(object):
    def __init__(self, *args):
        super(InfoMemory, self).__init__(*args)

    def virtual_memory(self):
        format_data = self.__format(psutil.virtual_memory()._asdict())
        return format_data

    def swap_memory(self, unit=None):
        format_data = self.__format(psutil.swap_memory()._asdict())
        return format_data

    def all(self):
        virtual = self.virtual_memory()
        swap = self.swap_memory()
        return dict(virtual=virtual, swap=swap)

    def __format(self, memory_info):
        for info, data in memory_info.items():
            if info != "percent":
                memory_info[info] = self.__convert(data)

        return memory_info

    def __convert(self, data):
        symbols = ("K", "M", "G", "T", "P", "E", "Z", "Y")
        prefix = {}
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10
        for s in reversed(symbols):
            if data >= prefix[s]:
                value = float(data) / prefix[s]
                return "%.1f%s" % (value, s)
        return "%sB" % data


InfoMemoryInst = InfoMemory()

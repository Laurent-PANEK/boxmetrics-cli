import psutil
import os


class InfoDisks(object):
    def __init__(self, *args):
        super(InfoDisks, self).__init__(*args)

    def __get_partition(self):
        for part in psutil.disk_partitions(all=False):
            part = part._asdict()
            if os.name == "nt":
                if "cdrom" in part["opts"] or part["fstype"] == "":
                    continue
            usage = self.__format(psutil.disk_usage(part["mountpoint"])._asdict())
            part["usage"] = usage

            yield part

    def all(self):
        return list(self.__get_partition())

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


InfoDisksInst = InfoDisks()

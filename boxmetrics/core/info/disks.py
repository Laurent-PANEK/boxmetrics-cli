import psutil
import os
from .base import Info


class Disks(Info):
    def __init__(self, *args):
        super(Disks, self).__init__(*args)

    def __get_partition(self):
        for part in psutil.disk_partitions(all=False):
            part = part._asdict()
            if os.name == "nt":
                if "cdrom" in part["opts"] or part["fstype"] == "":
                    continue
            usage = self._format(psutil.disk_usage(part["mountpoint"])._asdict())
            part["usage"] = usage

            yield part

    def partitions(self):
        return list(self.__get_partition())

    def stats(self):
        system = psutil.disk_io_counters()._asdict()

        perdisk = psutil.disk_io_counters(True)

        for disk, info in perdisk.items():
            perdisk[disk] = info._asdict()

        return dict(total=system, disks=perdisk)

    def all(self):
        return dict(partitions=self.partitions(), stats=self.stats())


DisksInst = Disks()

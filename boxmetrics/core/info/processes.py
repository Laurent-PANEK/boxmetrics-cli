import psutil
from typing import List, Dict
from .base import Info


class Processes(Info):
    def __init__(self, *args):
        super(Processes, self).__init__(*args)

    def all(self, filters: Dict = None) -> List[Dict]:
        """
        Return all processes informations
        
        :param filters: conditions that return processess must have, defaults to None
        :param filters: Dict, optional
        :return: List of processes
        :rtype: List[Dict]
        """

        processes = list()
        attrs = [
            "pid",
            "ppid",
            "status",
            "cpu_percent",
            "memory_percent",
            "name",
            "username",
        ]

        if not psutil.WINDOWS:
            attrs.append("uids")
            attrs.append("gids")

        for process in psutil.process_iter():
            proc = process.as_dict(attrs=attrs)
            if self._is_display(proc, filters):
                processes.append(proc)
        return processes

    def _is_display(self, data: Dict, filters: Dict = None) -> bool:
        if filters is None:
            return True
        for f, v in filters.items():
            if data[f] != v:
                return False
        return True


ProcessesInst = Processes()

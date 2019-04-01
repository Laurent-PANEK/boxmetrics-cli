import datetime
from typing import Dict, TypeVar

Number = TypeVar("Number", int, float)


class Info(object):
    def __init__(self, *args):
        super(Info, self).__init__(*args)

    def _format(self, dictItem: Dict, is_speed: bool = False) -> Dict:
        for info, data in dictItem.items():
            if is_speed:
                dictItem[info] = self._convert_bytes_per_second(data)
            else:
                if info != "percent":
                    dictItem[info] = self._convert_bytes(data)
        return dictItem

    def _format_date(self, timestamp: Number) -> str:
        return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

    def _convert_bytes(self, data: float) -> str:
        symbols = ("K", "M", "G", "T", "P", "E", "Z", "Y")
        prefix = {}
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10
        for s in reversed(symbols):
            if data >= prefix[s]:
                value = float(data) / prefix[s]
                return "%.2f%s" % (value, s)
        return "%.2fB" % data

    def _convert_bytes_per_second(self, data: float) -> str:
        symbols = ("K", "M", "G", "T", "P", "E", "Z", "Y")
        prefix = {}
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10
        for s in reversed(symbols):
            if data >= prefix[s]:
                value = float(data) / prefix[s]
                return "%.2f %s/s" % (value, s)
        return "%.2f B/s" % (data)

    def _zip_dict(self, first: Dict, second: Dict) -> Dict:
        zip = dict()
        if len(first.keys()) != len(second.keys()):
            return dict()

        for key in first.keys():
            zip[key] = (first[key], second[key])

        return zip

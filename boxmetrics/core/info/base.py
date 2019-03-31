import datetime

class Info(object):
    def __init__(self, *args):
        super(Info, self).__init__(*args)

    def _format(self, dictItem, is_speed=False):
        for info, data in dictItem.items():
            if is_speed:
                dictItem[info] = self.__convert_bytes_per_second(data)
            else:
                if info != "percent":
                    dictItem[info] = self.__convert_bytes(data)
        return dictItem
    
    def _format_date(self, timestamp):
        return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

    def __convert_bytes(self, data):
        symbols = ("K", "M", "G", "T", "P", "E", "Z", "Y")
        prefix = {}
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10
        for s in reversed(symbols):
            if data >= prefix[s]:
                value = float(data) / prefix[s]
                return "%.1f%s" % (value, s)
        return "%sB" % data

    def __convert_bytes_per_second(self, data):
        symbols = ("K", "M", "G", "T", "P", "E", "Z", "Y")
        prefix = {}
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10
        for s in reversed(symbols):
            if data >= prefix[s]:
                value = float(data) / prefix[s]
                return "%.2f%s/s" % (value, s)
        return "%.2f B/s" % (data)

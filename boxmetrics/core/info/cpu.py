import psutil


class InfoCPU(object):
    def __init__(self, *args):
        super(InfoCPU, self).__init__(*args)

    def percent(self, details):
        cpu = psutil.cpu_percent(percpu=details)
        return cpu

    def frequence(self, details):
        cpu_freq = psutil.cpu_freq(percpu=details)
        if details:
            for i, cpu in enumerate(cpu_freq):
                cpu_freq[i] = cpu._asdict()
        else:
            cpu_freq = cpu_freq._asdict()

        return cpu_freq

    def count_logical(self):
        return psutil.cpu_count()

    def count_physical(self):
        return psutil.cpu_count(False)

    def count(self):
        return dict(logical=self.count_logical(), physical=self.count_physical())

    def stats(self):
        return psutil.cpu_stats()._asdict()

    def all(self, details):
        percent = self.percent(details)
        freq = self.frequence(details)
        count = self.count()
        stats = self.stats()
        return dict(percent=percent, frequence=freq, count=count, stats=stats)


InfoCPUInst = InfoCPU()

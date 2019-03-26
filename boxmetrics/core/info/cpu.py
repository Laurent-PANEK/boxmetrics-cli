import psutil


class InfoCPU(object):
    def __init__(self, *args):
        super(InfoCPU, self).__init__(*args)

    def percent(self, details):
        cpu = psutil.cpu_percent(percpu=details)
        return dict(percent=cpu)

    def frequence(self, details):
        cpu = psutil.cpu_freq(percpu=details)
        return dict(frequence=cpu)

    def count_logical(self):
        return dict(logical=psutil.cpu_count())

    def count_physical(self):
        return dict(physical=psutil.cpu_count(False))

    def count(self):
        return dict({**self.count_logical(), **self.count_physical()})

    def stats(self):
        return dict(stats=psutil.cpu_stats())

    def all(self):
        return dict(
            {**self.stats(), **self.frequence(True), **self.percent(True)},
            count=self.count(),
        )


InfoCPUInst = InfoCPU()

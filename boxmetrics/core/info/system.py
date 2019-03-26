import psutil
import datetime


class InfoSystem(object):
    def __init__(self, *args):
        super(InfoSystem, self).__init__(*args)

    def boot_timestamp(self):
        return dict(timestamp=psutil.boot_time())

    def boot_time(self):
        return dict(
            format=datetime.datetime.fromtimestamp(psutil.boot_time()).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )

    def time(self):
        return dict({**self.boot_time(), **self.boot_timestamp()})

    def log_users(self):
        return dict(users=psutil.users())

    def all(self):
        return dict(self.log_users(), time=self.time())


InfoSystemInst = InfoSystem()

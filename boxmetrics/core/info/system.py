import psutil
import datetime


class InfoSystem(object):
    def __init__(self, *args):
        super(InfoSystem, self).__init__(*args)

    def boot_timestamp(self):
        return psutil.boot_time()

    def boot_time(self):
        return self.__format_date(self.boot_timestamp())

    def time(self):
        return dict(format=self.boot_time(), timestamp=self.boot_timestamp())

    def log_users(self):
        users = psutil.users()
        for i, user in enumerate(users):
            users[i] = user._asdict()
            users_started = users[i]["started"]
            users[i]["started"] = dict(
                format=self.__format_date(users_started), timestamp=users_started
            )

        return users

    def all(self):
        return dict(users=self.log_users(), time=self.time())

    def __format_date(self, timestamp):
        return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


InfoSystemInst = InfoSystem()

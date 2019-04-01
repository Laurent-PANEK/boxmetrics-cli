import psutil
from .base import Info


class System(Info):
    def __init__(self, *args):
        super(System, self).__init__(*args)

    def boot_timestamp(self):
        return psutil.boot_time()

    def boot_time(self):
        return self._format_date(self.boot_timestamp())

    def time(self):
        return dict(format=self.boot_time(), timestamp=self.boot_timestamp())

    def log_users(self):
        users = psutil.users()
        for i, user in enumerate(users):
            users[i] = user._asdict()
            users_started = users[i]["started"]
            users[i]["started"] = dict(
                format=self._format_date(users_started), timestamp=users_started
            )

        return users

    def all(self):
        return dict(users=self.log_users(), time=self.time())


SystemInst = System()

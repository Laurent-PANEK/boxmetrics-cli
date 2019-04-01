import psutil
from .base import Info


class Sensor(Info):
    def __init__(self, *args):
        super(Sensor, self).__init__(*args)

    def temp(self):
        if psutil.WINDOWS:
            return dict()

        temp = psutil.sensors_temperatures()

        for key, data in temp.items():
            temp[key] = data._asdict()

        return temp

    def fans(self):
        if psutil.WINDOWS:
            return dict()

        fans = psutil.sensors_fans()

        for key, data in fans.items():
            fans[key] = data._asdict()

        return fans

    def battery(self):
        battery = psutil.sensors_battery()

        battery = battery._asdict()
        battery["secsleft"] = self.__convert_remaining_time(battery["secsleft"])

        return battery

    def __convert_remaining_time(self, secs):
        value = {
            psutil.POWER_TIME_UNKNOWN: "?",
            psutil.POWER_TIME_UNLIMITED: "unlimited",
        }
        if secs in value.keys():
            return value[secs]

        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%dh%02dm%02ds" % (hh, mm, ss)

    def all(self):
        temp = self.temp()
        fans = self.fans()
        battery = self.battery()

        return dict(temperature=temp, fans=fans, battery=battery)


SensorInst = Sensor()

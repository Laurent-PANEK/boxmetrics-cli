from cement import App, Controller, ex
from boxmetrics.core.info.sensor import SensorInst as infoSensor


class Sensor(Controller):
    class Meta:
        label = "sensor"
        stacked_on = "info"
        stacked_type = "nested"
        description = "Get sensor info"

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.render(infoSensor.all())

    @ex(help="get hardware temperature")
    def temperature(self):
        self.app.render(infoSensor.temp())

    @ex(help="get fans info")
    def fans(self):
        self.app.render(infoSensor.fans())

    @ex(help="get battery info")
    def battery(self):
        self.app.render(infoSensor.battery())

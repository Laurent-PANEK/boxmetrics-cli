from cement import App, Controller, ex
from boxmetrics.core.info.sensors import SensorsInst as infoSensors


class Sensors(Controller):
    class Meta:
        label = "sensors"
        stacked_on = "info"
        stacked_type = "nested"
        description = "Get sensors info"

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.render(infoSensors.all())

    @ex(help="get hardware temperature")
    def temperature(self):
        self.app.render(infoSensors.temp())

    @ex(help="get fans info")
    def fans(self):
        self.app.render(infoSensors.fans())

    @ex(help="get battery info")
    def battery(self):
        self.app.render(infoSensors.battery())

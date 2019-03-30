from cement import App, Controller, ex
from boxmetrics.core.info.disks import InfoDisksInst as infoDisks


class Disks(Controller):
    class Meta:
        label = "disks"
        stacked_on = "info"
        stacked_type = "nested"
        description = "Get disks info"

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.render(infoDisks.all())

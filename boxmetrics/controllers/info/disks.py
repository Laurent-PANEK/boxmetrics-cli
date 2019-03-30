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

    @ex(help="get partitions info")
    def partitions(self):
        self.app.render(infoDisks.partitions())

    @ex(help="get stats of disks")
    def stats(self):
        self.app.render(infoDisks.stats())

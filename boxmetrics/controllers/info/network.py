from cement import App, Controller, ex
from boxmetrics.core.info.network import NetworkInst as infoNetwork


class Network(Controller):
    class Meta:
        label = "network"
        stacked_on = "info"
        stacked_type = "nested"
        description = "Get network info"

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.render(infoNetwork.all())

    @ex(help="get network stats")
    def stats(self):
        self.app.render(infoNetwork.stats())

    @ex(help="get network config")
    def config(self):
        self.app.render(infoNetwork.config())

from cement import App, Controller, ex
from boxmetrics.core.info.memory import InfoMemoryInst as infoMemory


class Memory(Controller):
    class Meta:
        label = "memory"
        stacked_on = "info"
        stacked_type = "nested"
        description = "Get memory info"

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.render(infoMemory.all())

    @ex(
        help="get virtual memory info",
    )
    def virtual(self):
        self.app.render(infoMemory.virtual_memory())

    @ex(
        help="get swap memory info"
    )
    def swap(self):
        self.app.log.info("swap memory")
        self.app.render(infoMemory.swap_memory())

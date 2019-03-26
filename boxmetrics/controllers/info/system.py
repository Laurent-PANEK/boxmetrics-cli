from cement import App, Controller, ex
from boxmetrics.core.info.system import InfoSystemInst as infoSys


class System(Controller):
    class Meta:
        label = "system"
        stacked_on = "info"
        stacked_type = "nested"
        description = "Get system info"

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.render(infoSys.all())

    @ex(
        help="get boot time info",
        arguments=[
            (
                ["-f", "--format"],
                {"help": "only format boot time", "action": "store_true"},
            ),
            (
                ["-t", "--timestamp"],
                {"help": "only timestamp boot time", "action": "store_true"},
            ),
        ],
    )
    def time(self):
        self.app.log.info("boot time")
        if self.app.pargs.format:
            self.app.render(infoSys.boot_time())
        elif self.app.pargs.timestamp:
            self.app.render(infoSys.boot_timestamp())
        else:
            self.app.render(infoSys.time())

    @ex(help="get connected users")
    def users(self):
        self.app.render(infoSys.log_users())

from cement import App, Controller, ex
from boxmetrics.core.info.cpu import CPUInst as infoCPU


class CPU(Controller):
    class Meta:
        label = "cpu"
        stacked_on = "info"
        stacked_type = "nested"
        description = "Get CPU info"

        arguments = [
            (
                ["-D", "--details"],
                {"help": "enable per cpu details", "action": "store_true"},
            )
        ]

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.render(infoCPU.all(self.app.pargs.details))

    @ex(
        help="get cpu usage",
        arguments=[
            (
                ["-D", "--details"],
                {"help": "show per cpu usage", "action": "store_true"},
            )
        ],
    )
    def percent(self):
        self.app.render(infoCPU.percent(self.app.pargs.details))

    @ex(
        help="get cpu frequence",
        arguments=[
            (
                ["-D", "--details"],
                {"help": "show per cpu frequence (unix only)", "action": "store_true"},
            )
        ],
    )
    def frequence(self):
        self.app.log.info("cpu frequence")
        self.app.render(infoCPU.frequence(self.app.pargs.details))

    @ex(
        help="number of cpu",
        arguments=[
            (["-l", "--logical"], {"help": "only logical cpu", "action": "store_true"}),
            (
                ["-p", "--physical"],
                {"help": "only physical cpu", "action": "store_true"},
            ),
        ],
    )
    def count(self):
        if self.app.pargs.logical:
            self.app.render(infoCPU.count_logical())
        elif self.app.pargs.physical:
            self.app.render(infoCPU.count_physical())
        else:
            self.app.render(infoCPU.count())

    @ex(help="CPU stats")
    def stats(self):
        self.app.render(infoCPU.stats())

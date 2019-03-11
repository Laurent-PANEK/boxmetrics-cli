from cement import App, Controller, ex


class Install(Controller):
    class Meta:
        label = "inside"
        stacked_on = "base"
        stacked_type = "embedded"

    @ex(
        help="install boxmetrics client service",
        arguments=[
            (
                ["mode"],
                {
                    "nargs": "?",
                    "help": "install mode (default: %(default)s)",
                    "action": "store",
                    "choices": ["ssh", "agent"],
                    "default": "ssh",
                },
            )
        ],
    )
    def install(self):
        if self.app.pargs.mode is not None:
            mode = self.app.pargs.mode
        self.app.log.info("install {} mode".format(mode))


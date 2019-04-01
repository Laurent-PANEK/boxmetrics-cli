from cement import App, Controller, ex
from boxmetrics.core.info.processes import ProcessesInst as infoProcesses
import argparse


class StoreDict(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        dest_dict = getattr(namespace, self.dest, {})

        if dest_dict is None:
            dest_dict = {}

        dest_dict[self.metavar] = values
        setattr(namespace, self.dest, dest_dict)


class Processes(Controller):
    class Meta:
        label = "processes"
        stacked_on = "info"
        stacked_type = "nested"
        description = "Get processes info"

        arguments = [
            (
                ["-u", "--username"],
                {
                    "help": "Filter processes on username",
                    "action": StoreDict,
                    "dest": "filters",
                    "metavar": "username",
                },
            ),
            (
                ["-n", "--name"],
                {
                    "help": "Filter processes on name",
                    "action": StoreDict,
                    "dest": "filters",
                    "metavar": "name",
                },
            ),
            (
                ["-s", "--status"],
                {
                    "help": "Filter processes on status",
                    "action": StoreDict,
                    "choices": [
                        "running",
                        "sleeping",
                        "stopped",
                        "zombie",
                        "dead",
                        "waking",
                        "parked",
                        "idle",
                        "locked",
                        "waiting",
                        "suspended",
                    ],
                    "dest": "filters",
                    "metavar": "status",
                },
            ),
        ]

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.render(infoProcesses.all(self.app.pargs.filters))

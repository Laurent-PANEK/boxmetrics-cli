from cement import App, Controller, ex
from boxmetrics.core.info.full import full


class Info(Controller):
    class Meta:
        label = "info"
        stacked_on = "base"
        stacked_type = "nested"
        description = "Get server info"

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.render(full)


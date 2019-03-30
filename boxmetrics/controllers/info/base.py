from cement import App, Controller, ex


class Info(Controller):
    class Meta:
        label = "info"
        stacked_on = "base"
        stacked_type = "nested"
        description = "Get server info"


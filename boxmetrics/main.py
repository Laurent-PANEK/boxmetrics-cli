from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from .core.exc import BoxmetricsError
from .controllers.base import Base
from .controllers.info.base import Info
from .controllers.info.system import System

# configuration defaults
CONFIG = init_defaults("boxmetrics")
CONFIG["boxmetrics"]["foo"] = "bar"


class Boxmetrics(App):
    """Boxmetrics CLI primary application."""

    class Meta:
        label = "boxmetrics"

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        close_on_exit = True

        # load additional framework extensions
        extensions = ["yaml", "colorlog", "json"]

        # configuration handler
        config_handler = "yaml"

        # configuration file suffix
        config_file_suffix = ".yml"

        # set the log handler
        log_handler = "colorlog"

        # set the output handler
        output_handler = "json"

        # register handlers
        handlers = [Base, Info, System]


class BoxmetricsTest(TestApp, Boxmetrics):
    """A sub-class of Boxmetrics that is better suited for testing."""

    class Meta:
        label = "boxmetrics"


def main():
    with Boxmetrics() as app:
        try:
            app.run()

        except AssertionError as e:
            print("AssertionError > %s" % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback

                traceback.print_exc()

        except BoxmetricsError as e:
            print("BoxmetricsError > %s" % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback

                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print("\n%s" % e)
            app.exit_code = 0


if __name__ == "__main__":
    main()

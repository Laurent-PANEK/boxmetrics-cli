from cement.utils.version import get_version as cement_get_version
import re

__version__ = "0.0.1-alpha.0"


def parse_version(version):
    parsed_version = re.compile(r"\.|\-").split(version)

    if len(parsed_version) == 3:
        parsed_version.append("final")

    return tuple(parsed_version)


VERSION = parse_version(__version__)


def get_normalize_version(version=VERSION):
    return cement_get_version(version)


def get_version(version=__version__):
    return version

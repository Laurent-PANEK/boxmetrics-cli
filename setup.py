from setuptools import setup, find_packages
from boxmetrics.core.version import get_normalize_version

VERSION = get_normalize_version()

f = open("README.md", "r")
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name="boxmetrics",
    version=VERSION,
    description="CLI for Boxmetrics Application",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Boxmetrics Team",
    author_email="team@boxmetrics.ml",
    url="https://github.com/boxmetrics/boxmetrics-cli",
    license="MIT",
    packages=find_packages(exclude=["ez_setup", "tests*"]),
    package_data={"boxmetrics": ["templates/*", "scripts/*"]},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        boxmetrics = boxmetrics.main:main
    """,
)

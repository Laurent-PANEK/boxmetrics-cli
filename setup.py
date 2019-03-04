
from setuptools import setup, find_packages
from boxmetrics-cli.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='boxmetrics-cli',
    version=VERSION,
    description='CLI for Boxmetrics Application',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Boxmetrics Team',
    author_email='team@boxmetrics.ml',
    url='https://github.com/Laurent-PANEK/boxmetrics-cli',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'boxmetrics-cli': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        boxmetrics-cli = boxmetrics-cli.main:main
    """,
)

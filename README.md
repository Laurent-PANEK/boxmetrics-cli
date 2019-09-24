# CLI for Boxmetrics Application

 > This repo is not maintain anymore and had been replaced by new boxmetrics cli write in go 👉 <https://github.com/boxmetrics/boxmetrics-cli>

## Installation

```text

# install with pip

$ pip install -r requirements.txt

$ pip install setup.py
```

## Development

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

Linter :

- pylint
- mypy

Code formatter :

- black

### Environment Setup

The following demonstrates setting up and working with a development environment:

```text
### create a virtualenv for development

$ make virtualenv

$ source env/bin/activate


### run boxmetrics cli application

$ boxmetrics --help


### run pytest / coverage

$ make test
```

### Releasing to PyPi

Before releasing to PyPi, you must configure your login credentials:

**~/.pypirc**:

```text
[pypi]
username = YOUR_USERNAME
password = YOUR_PASSWORD
```

Then use the included helper function via the `Makefile`:

```text
### build binaries files

$ make dist

### upload to Pypi

$ make dist-upload
```

## Deployments

### Docker

Included is a basic `Dockerfile` for building and distributing `Boxmetrics CLI`,
and can be built with the included `make` helper:

```text

### build docker image

$ make docker

$ docker run -it boxmetrics --help
```

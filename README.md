# flir_test_2

The second technical test from Teledyne FLIR


## Installation and Usage

Requires Python 3.8.


### Installation

Please follow the [Development](#development) instructions, below.

In the future, this project might be available on our local PyPI server or
might be distributed as a frozen EXE.


### Usage

A CLI entry point exists for this project. In a linux shell with the activated
virtual environment, run `flir`:

```
$ flir
Usage: flir [OPTIONS] FILENAME
Try 'flir --help' for help.

Error: Missing argument 'FILENAME'.
```

You can run `flir --help` to get additional information.


## Development

1.  Clone the repo: `git clone `
2.  Move into that dir: `cd flir_test_2`
3.  Create a virtual environment: `python -m venv .venv`
4.  Activate it: `. .venv/bin/activate`
5.  Install python packages:
    1.  `pip install -U pip setuptools wheel`
    2.  `pip install -r requirements.txt -r requirements-dev.txt`
    3.  `pip install -e .`
6.  Install the pre-commit hooks: `pre-commit install`
7.  Run tests to verify: `pytest`
8.  Ready to develop


## Changelog

See [CHANGELOG.md](.\CHANGELOG.md).

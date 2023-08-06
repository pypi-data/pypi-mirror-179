# Ultimate PyFoam

https://doc.cfd.direct/openfoam/user-guide-v8/basic-file-format

[![PyPI](https://img.shields.io/pypi/v/py2of.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/py2of.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/py2of)][pypi status]
[![License](https://img.shields.io/pypi/l/py2of)][license]

[![Read the documentation at https://py2of.readthedocs.io/](https://img.shields.io/readthedocs/py2of/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/ARostekMU/py2of/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/ARostekMU/py2of/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/py2of/
[read the docs]: https://py2of.readthedocs.io/
[tests]: https://github.com/ARostekMU/py2of/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/ARostekMU/py2of
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Features

- TODO

## Requirements

- TODO

## Installation

You can install _Ultimate PyFoam_ via [pip] from [PyPI]:

```console
$ pip install py2of
```

## Usage

Please see the [Command-line Reference] for details.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Ultimate PyFoam_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/ARostekMU/py2of/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/ARostekMU/py2of/blob/main/LICENSE
[contributor guide]: https://github.com/ARostekMU/py2of/blob/main/CONTRIBUTING.md
[command-line reference]: https://py2of.readthedocs.io/en/latest/usage.html

## Python virtual environment cheatsheet

Which **python**/**pip** am I using?

```
which python
which pip
```

List python packages installed using **pip**

```
pip list
```

Use **venv** to create new virtual environment called for example test_env in the current working directory

```
python -m venv test_env
```

Start using test_env virtual environment

```
source test_env/bin/activate
```

`which python` should now show you the path to /something/test_env/bin/python

If you now do for example `pip install numpy`, **numpy** will be installed only into the test_env virtual environment. `pip list` will show that only **pip**, **setuptools** and **numpy** are installed.

Stop working in the current virtual environment

```
deactivate
```

Install another python version, for example 3.11.0

```
pyenv install 3.11.0
```

List installed python versions

```
pyenv versions
```

Start using python 3.11.0

```
pyenv local 3.11.0
```

Command `python` should now open a **python shell** on version 3.11.0

Now you should be able to create a virtual environment with this new python version :)

<br></br>

**Poetry** is a tool for dependency management and packaging in Python. Moreover, it can create it's own virtual environments, which makes your life easier.
If you're in a folder of a project which uses **Poetry** (for example the Claudio's template we're using is such a project), you can find out
which virtual environment this project is using by

```
poetry env info
```

If you want to start using this environment in your terminal, you don't have to do the whole `source /something/activate` thing anymore, you can just type

```
poetry shell
```

and the environment will be activated.

If you want to update a package, or a python version, you can do so manually in a file _pyproject.toml_. For example, you might rewrite python version from ^3.7 to ^3.8.
If you update the _pyproject.toml_ like this, you must update _poetry.lock_ by doing

```
poetry lock
```

In _poetry.lock_ you can find all the packages and versions which your project is using. In order to add a new package, for example **numpy**, type

```
poetry add numpy
```

If you don't know which command to use, or what all the possibilities offered by the tool you are using are, there are multiple sources where to look.

You can always try to run the tool with no arguments like this (not just **poetry**):

```
poetry
```

which usually outputs some information about usage and a list of available commands.

If that is not enough, there is usually some kind of official documentation which is only one google search away: https://python-poetry.org/docs/basic-usage/

In case of desperation, you might want to try going to Stack Overflow https://stackoverflow.com/.

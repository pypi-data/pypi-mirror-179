[![Tests](https://github.com/UB-Quantic/pypickup/actions/workflows/python-testing.yml/badge.svg)](https://github.com/UB-Quantic/pypickup/actions/workflows/python-testing.yml)
[![Coverage](https://github.com/UB-Quantic/pypickup/actions/workflows/python-coverage.yml/badge.svg)](https://github.com/UB-Quantic/pypickup/actions/workflows/python-coverage.yml)

# pypickup

A tool to download packages from PyPI and save them locally, building a directory tree that fulfills [PEP 503](https://peps.python.org/pep-0503/). Properly configured, `pip` will install packages from there as if it was downloading them from the PyPI repository itself.

For example, the following commands will download all final versions (no `dev` and no `rc` versions), source distributions of `numpy` into the `.pypickup` folder, and then install the latest compatible version from there.

```
pypickup add -s -p ./.pypickup numpy
pip install --index-url ./.pypickup numpy
```

In order to save yourself from typing the -p parameter every time, you can just set an env variable PYPICKUP_INDEX_PATH (which you can include in your ~/.bashrc file if you feel like it):

```
export PYPICKUP_INDEX_PATH=/usr/local/pypickup
```

## Install

Before installing pypickup you should do:

```
export PYPICKUP_INDEX_PATH=MY_LOCAL_REPOSITORY_PATH
```

Then:
```
pip install pypickup
```

Alternatively, you can download this repository and perform an editable installation:

```
pip install --editable .
```

## Commands

An -h flag can be used on any command to display all the available options and its usage. For instance:

```
pypickup add -h
```

To add a package for the first time:

```
pypickup add numpy
```

This will create a folder in the default location (./.pypickup/) in which all the stablished files (.whl and .zip) for the specified package will be downloaded. Besides, it will create the corresponding metadata files (index.html) to track that package. The next time you want to synchronize the same package against the PyPI remote repository, you should do:

```
pypickup update numpy
```

This will download the new packages available in the remote, in case there is any. It'll do nothing otherwise. It also updates the index.html of the indicated package with the new downloaded packages, as expected.

To redefine another default location we may set an environment variable PYPICKUP_INDEX_PATH. 

2 more commands are available to remove packages and to list the available ones already added:

```
pypickup rm numpy

pypickup list
```

If we specify a package for the 'list' command, it will show a list of the downloaded distributions themselves.

```
pypickup list numpy
```

And additional command is in development to configure the settings file for the wheels filtering.

```
pypickup config -h
```

## Examples

To check what are all the available packages in the remote repository and which of them would be downloaded:

```
pypickup add -a --dry-run [package]
```

## Development

### Add new commands

To add new commands to the application, follow these steps:

1. Create a new \[commandName\].py file with a class named \[commandName\]EP (standing for EntryPoint), which should include 2 main methods: `init_subparser(...)` and `run(...)`. These methods will be automatically called by the `cli()` method at cli.py, which will be in turn called by the main script at \_\_main\_\_.py.
2. Add the new command entry in the pyproject.toml file, in the list [project.entry-points."pypickup.cmd"].
3. Add the corresponding export in the pypickup/cmd/\_\_init\_\_.py file.
4. Finally, create a new class in the controller.py that will implement the specific methods for that command. This new class should inherit from the general-purpose class LocalPyPIController and should implement, at least, a method `parseScriptArguments(...)`. This class LocalPyPIController should:
    - Add in their \_\_init\_\_(self) method the arguments for the new command you are coding.
    - Implement the getters and setters for the new command, which should be used in your new class.

    Your new class should parse **all** the arguments your command is going to use in your own method `parseScriptArguments(...)`. If some of the arguments already exist (from other commands), you use them but you should parse them anyway in your `parseScriptArguments(...)`, even if this implies "repeating" some code. This is the best approach for an application open to new features.

    Apart from the main controller file, there are 2 other controllers that should be considered properly when adding new commands/features.
    - htmlManager.py: in charge of everything related with the HTML files management. It already include methods to find, insert and delete tags into an HTML string body.
    - networkManager.py: in charge of everything related with the network (e.g. getting URL links).

### Editable installation

In order to speed up the development, we recommend an editable installation:

```
pip install --editable .
```
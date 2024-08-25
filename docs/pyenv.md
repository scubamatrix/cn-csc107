# pyenv

[pyenv](https://github.com/pyenv/pyenv) allows you to switch between multiple versions of Python. 

`pyenv` is simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well.

This project was forked from `rbenv` and `ruby-build` and modified for Python.


## Windows Note

Pyenv does not officially support Windows and does not work in Windows outside the Windows Subsystem for Linux (WSL). 

In addition, the Python versions pyenv installs are not native Windows versions but rather Linux versions running in a virtual machine -- so you will not get Windows-specific functionality.


If you are using Windows, we recommend using [pyenv-win](https://github.com/pyenv-win/pyenv-win) fork which does install native Windows Python versions.


## Install pyenv

```zsh
    # Linux and macOS
    brew update && brew install pyenv    
    brew install openssl readline sqlite3 xz zlib tcl-tk

    # install prerequisites for python build
    sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

```zsh
    # create virtual environment
    python3 -m venv ~/pyenv/coreml       # create venv
    source ~/pyenv/coreml/bin/activate   # activate the virtual environment
    pip install -U pip                   # update pip
    pip install -r reqs.txt              # install dependencies
    deactivate                           # deactivate

    pip install --upgrade pip

    # install/update python environment
    pyenv install 3.8.13
    pyenv local 3.8.13

    pip install tensorflow
    pip install tensorflow-metal
```

```bash
    pip list --format=freeze  > metal-venv.txt
    pip install -r metal-venv.txt
```


## Commands

```zsh
    # Install the required Python version
    pyenv install 3.9.0

    # Refresh pyenv since you installed a new Python version
    pyenv rehash

    # Set global Python version
    pyenv global 3.9.0

    # Set local Python version for project
    pyenv local 3.11

    # List of python versions installed
    pyenv versions

    # Confirm Python version
    pyenv version
    # 3.9.0 (set by ~/.pyenv/version)
```

```bash
    pyenv versions
    python -V

    which python        # ~/.pyenv/shims/python

    pyenv which python  # /usr/bin/python
    pyenv which pip

    # upgrade pip
    pip install --upgrade pip

    pyenv install --list | grep "3\.11.*"

    # specify python version
    pyenv install -v 3.11
    pyenv uninstall 2.7.15

    pyenv global 3.11.4  # set global Python version
    pyenv local 3.9      # set application Python version
    python -V
    pyenv versions

    pyenv global system  # reset to system default

    ls ~/.pyenv/versions/

    python -m test  # verify python install
```

```bash
    cd repos/stocks
    pyenv local 3.11.4
    pyenv which python
```

---------


## What pyenv does

- Lets you change the global Python version on a per-user basis.

- Provides support for per-project Python versions.

- Allows you to override the Python version with an environment variable.

- Searches for commands from multiple versions of Python at a time which may be helpful to test across Python versions with tox.


## In contrast with pythonbrew and pythonz, pyenv does not ...

- Depend on Python itself. pyenv was made from pure shell scripts. There is no bootstrap problem of Python.

- Need to be loaded into your shell. Instead, pyenv's shim approach works by adding a directory to your PATH.

- Manage virtualenv. Of course, you can create virtualenv yourself, or pyenv-virtualenv to automate the process.


## Understanding Shims

pyenv works by inserting a directory of shims at the front of your PATH:

```bash
    $(pyenv root)/shims:/usr/local/bin:/usr/bin:/bin
```

Through a process called _rehashing_, pyenv maintains shims in that directory to match every Python command across every installed version of Python—python, pip, etc.

_Shims_ are lightweight executables that simply passe your command along to pyenv. If `pyenv` installed, then your operating system will perform the following when you run the `pip` command:

- Search your PATH for an executable file named pip.

- Find the pyenv shim named pip at the beginning of your PATH.

- Run the shim named pip which in turn passes the command along to pyenv.


## Understanding Python version selection

When you execute a shim, pyenv determines which Python version to use by reading it from the following sources, in this order:

1. The `PYENV_VERSION` environment variable (if specified). You can use the `pyenv shell` command to set this environment variable in your current shell session.

2. The application-specific `.python-version` file in the current directory (if present). You can modify the current directory's `.python-version` file with the `pyenv local` command.

3. The first `.python-version` file found (if any) by searching each parent directory until reaching the root of your filesystem.

4. The global `$(pyenv root)/version` file. You can modify this file using the `pyenv global` command. If the global version file is not present, pyenv defaults to the "system" Python (see below).

A special version name `system` means to use whatever Python is found on `PATH` after the shims `PATH` entry (whatever would be run if Pyenv shims were not on PATH). 

Note that pyenv considers those installations outside its control and does not attempt to inspect or distinguish them in any way. So if you are on MacOS and have OS-bundled Python 3.8.9 and Homebrew-installed Python 3.9.12 and 3.10.2 -- for Pyenv, this is still a single "system" version and whichever of those is first on `PATH` under the executable name you specified will be run.

Shims also fall through to anything further on `PATH` if the corresponding executable is not present in any of the selected Python installations. This allows you to use any programs installed elsewhere on the system as long as they are not shadowed by a selected Python installation.

As far as Pyenv is concerned, version names are simply directories under `$(pyenv root)/versions`.

```bash
    python3 -m venv ~/pyenv/metal         # create virtual environment
    source ~/pyenv/metal/bin/activate     # activate virtual environment
    deactivate                            # deactivate

    source ~/pyenv/python-go/bin/activate   
    source ~/pyenv/metal/bin/activate 
    source ~/pyenv/stock/bin/activate
    source ~/pyenv/poetry_demo/bin/activate 

    python -m pip install -U pip            # update pip
    pip install -r requirements.txt         # install dependencies
```

```bash
    pyenv install 3.8.13    # install/update python environment
    pyenv uninstall 3.8.13  # uninstall python version

    pyenv local 3.8.13      # automatically select when you are in the current directory 
    pyenv shell 3.8.13      # select just for current shell session
    pyenv global 3.8.13     # select globally for your user account

    pyenv install 3.11.4
    pyenv shell 3.11.4

    pyenv shims  # list existing pyenv shims

    # display which real executable would be run
    # when you invoke <command> via a shim
    pyenv which python

    which python            # display path for current virtual environment
    pyenv version           # display the currently active Python version
    pyenv versions          # list all Python versions known to pyenv

    pyenv prefix            # display directories where the given Python versions are installed    
    pyenv root              # display root directory where versions and shims are kept
```


## Advanced Configuration

Also see the "Environment variables" section for the environment variables that control Pyenv behavior.

`pyenv init` is the only command that crosses the line of loading extra commands into your shell. 

Here is what `eval "$(pyenv init -)"` actually does:

1. **Sets up the shims path.** This is what allows Pyenv to intercept and redirect invocations of python, pip, etc. 

  This prepends `$(pyenv root)/shims` to your `$PATH`. 

  This also deletes any other instances of `$(pyenv root)/shims` on `PATH` which allows invoke ofl `eval "$(pyenv init -)"` multiple times without getting duplicate `PATH` entries.

2. **Installs autocompletion.** This is entirely optional but pretty useful. Sourcing `$(pyenv root)/completions/pyenv.bash` will set that up. There are also completions for Zsh and Fish.

3. **Rehashes shims.** From time to time you will need to rebuild your shim files. Doing this on init makes sure everything is up to date. You can always run `pyenv rehash` manually.

4. **Installs pyenv into the current shell as a shell function.** This is also optional but allows pyenv and plugins to change variables in your current shell. 

  This is required for some commands such as `pyenv shell` to work. 

  The sh dispatcher does not do anything crazy like override `cd` or hack your shell prompt, but if for some reason you need pyenv to be a real script rather than a shell function, you can safely skip it.

In contrast, `eval "$(pyenv init --path)"` only does items 1 and 3.

To see exactly what happens under the hood for yourself, run `pyenv init -` or `pyenv init --path`.

`eval "$(pyenv init -)" `is supposed to run at any interactive shell's startup (including nested shells -- e.g. those invoked from editors) so that you get completion and convenience shell functions.

`eval "$(pyenv init --path)"` can be used instead of eval "$(pyenv init -)" to just enable shims, without shell integration. It can also be used to bump shims to the front of PATH after some other logic has prepended stuff to PATH that may shadow Pyenv's shims.

- In Debian-based distributions, the stock `~/.profile` prepends per-user bin directories to `PATH` after having sourced `~/.bashrc`. 

- This necessitates appending a `pyenv init` call to `~/.profile` as well as `~/.bashrc` in these distributions because the system's Pip places executables for modules installed by a non-root user into those per-user `bin` directories.


## References

[1]: [pyenv](https://github.com/pyenv/pyenv)

[2]: [pyenv commands](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md)


# Poetry

[Poetry](https://github.com/python-poetry/poetry) is a tool for dependency management and packaging in Python. 

`poetry` allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

Poetry offers a lockfile to ensure repeatable installs and can build your project for distribution.

<!-- MarkdownTOC -->

- Commands
- Install Poetry
- What is pipx?
- Create environment
- Python Dependencies
- Default Directories
- Environments
- Troubleshooting
- Advanced Concepts
- Committing your poetry.lock file to version control
  - As an application developer
  - As a library developer
  - Installing dependencies only
- References

<!-- /MarkdownTOC -->



## Commands

```zsh  
  poetry shell  # activate venv
  exit          # deactivate venv

  source {path_to_venv}/bin/activate
  deactivate

  # update dependencies to latest versions
  poetry update

  pip install --upgrade pip
```

```zsh
  # default workflow
  pyenv install 3.11.8
  pyenv local 3.11.8

  # Set local Python version for project
  pyenv local 3.11.8
  poetry env use 3.11.8

  poetry shell
  poetry install
```

```zsh
  tree

  poetry add mypy --group dev

  poetry remove mypy

  # install dependencies
  poetry install

  # run programs
  poetry run python ./script.py
  poetry run black
  poetry run pytest

  poetry run python ./run_first.py
```

## Install Poetry

[pipx](https://github.com/pypa/pipx) — Install and Run Python Applications in Isolated Environments

`pipx` is used to install Python CLI applications globally while still isolating them in virtual environments. 

pipx will manage upgrades and uninstalls when used to install Poetry.


```zsh
  # Linux and macOS
  brew update && brew install pipx

  # Windows
  scoop install pipx

  pipx ensurepath
```

```zsh
  pipx install poetry
  pipx install poetry==1.2.0

  # update poetry
  pipx upgrade poetry

  pipx uninstall poetry
```


## What is pipx?

`pipx` is a tool to help you install and run end-user applications written in Python. 

[Comparison of pipx to other tools](https://pipx.pypa.io/stable/comparisons/)

pipx is roughly similar to macOS brew, JavaScript npx, and Linux apt.

pipx closely related to pip. In fact, pipx uses pip but pipx is focused on installing and managing Python packages that can be run from the command line directly as applications.

pip is a general-purpose package installer for both libraries and apps with no environment isolation. pipx is made specifically for application installation since it adds isolation yet still makes the apps available in your shell: pipx creates an isolated environment for each application and its associated packages.

By default, pipx uses the same package index as pip, PyPI. 

pipx can also install from all other sources pip can such as a local directory, wheel, git url, etc.


----------


## Create environment

By default, Poetry creates a virtual environment in `{cache-dir}/virtualenvs`. 

You can change the `cache-dir` value by editing the Poetry configuration. In addition, you can use the `virtualenvs.in-project` configuration variable to create virtual environments in your project directory.

Poetry will detect and respect an existing virtual environment that has been externally activated which is a powerful mechanism that is intended to be an alternative to Poetry’s simplified built-in environment management.

To take advantage of this feature, simply activate a virtual environment using your preferred method or tooling before running any Poetry commands that expect to manipulate an environment.

```zsh
  # create new blank project using poetry
  poetry new poetry-demo


  # use poetry with exisiting code
  cd poetry-demo
  git init

  cd github-code
  poetry init
```

## Python Dependencies

```zsh
  poetry add tensorflow==2.15 --group dev

  # poetry add tensorflow==2.14 --group dev
  # poetry add tensorflow-metal==1.1.0 --group dev
```

```zsh
  poetry add safety --group dev
  
  poetry run safety check

  poetry run nitpick fix
  poetry run nitpick check
```


## Default Directories

Application developers commit `poetry.lock` to version control to get more reproducible builds.

```zsh
  poetry config --list
```

```
  # macOS
  Cache:  ~/Library/Caches/pypoetry
  Config: ~/Library/Application Support/pypoetry
  Data:   ~/Library/Application Support/pypoetry


  # Linux
  Cache:  ~/.cache/pypoetry
  Config: ~/.config/pypoetry
  Data:   ~/.local/share/pypoetry

  # Windows
  Cache:  %LOCALAPPDATA%\pypoetry
  Config: %APPDATA%\pypoetry
  Data:   %APPDATA%\pypoetry

  # All (Linux / macOS / Windows)
  virtualenvs.path: {cache-dir}/virtualenvs
```


## Environments

```zsh
  poetry env info
  poetry env info --path

  poetry env list

  poetry env use 3.11

  # delete environment
  poetry env remove python3.7
  poetry env remove 3.7
  poetry env remove test-O3eWbxRl-py3.7
```


```zsh 
  poetry config cache-dir
  poetry cache list
  poetry cache clear pypi --all
```


```zsh
  poetry config --list

  # add or update config setting
  poetry config virtualenvs.path /path/to/cache/directory/virtualenvs

  # remove a config setting
  poetry config virtualenvs.path --unset
```


## Troubleshooting

```zsh
  # cleanup environments
  poetry env remove --all
  poetry cache clear --all .
  rm -rf $(poetry config cache-dir)/artifacts
```

```zsh
  # Fix poetry install pending
  export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring
  pyenv shell system
  python3 -m keyring --disable
```


----------



## Advanced Concepts

## Committing your poetry.lock file to version control

### As an application developer

Application developers commit poetry.lock to get more reproducible builds.

Committing this file to VC is important because it will cause anyone who sets up the project to use the exact same versions of the dependencies that you are using. Your CI server, production machines, other developers in your team, everything and everyone runs on the same dependencies, which mitigates the potential for bugs affecting only some parts of the deployments. Even if you develop alone, in six months when reinstalling the project you can feel confident the dependencies installed are still working even if your dependencies released many new versions since then. (See note below about using the update command.)

### As a library developer

Library developers have more to consider. Your users are application developers and your library will run in a Python environment you do not control.

The application ignores your library’s lock file which means it can use whatever dependency version meets the constraints in your `pyproject.toml`, but the application will probably use the latest compatible dependency version. 

If your library’s `poetry.lock` falls behind some new dependency version that breaks things for your users, you are likely to be the last to find out about it.

A simple way to avoid such a scenario is to omit the `poetry.lock` file. However, you will sacrifice reproducibility and performance to a certain extent. Without a lockfile, it can be difficult to find the reason for failing tests, because in addition to obvious code changes an unnoticed library update might be the culprit. In fact, Poetry will have to lock before installing a dependency if `poetry.lock` has been omitted. Depending on the number of dependencies, locking may take a significant amount of time.

If you do not want to give up the reproducibility and performance benefits, consider a regular refresh of `poetry.lock` to stay up-to-date and reduce the risk of sudden breakage for users.


### Installing dependencies only

The current project is installed in `editable` mode by default.

If you want to install the dependencies only, run the install command with the --no-root flag:

```zsh
  poetry install --no-root
```



## References

[1]: [Creating A Modern Python Development Environment](https://itnext.io/creating-a-modern-python-development-environment-3d383c944877)

[2]: [Poetry Docs](https://python-poetry.org/docs/basic-usage/)

[3]: [Comparison of pipx to other tools](https://pipx.pypa.io/stable/comparisons/)


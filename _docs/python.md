# Python

## Python Version and Package management

### 0. Summary

```shell

pyenv versions
pyenv install --list
pyenv install 3.8.0

pipenv --python 3.8.0
pipenv install -r requirements.txt
pipenv graph
pipenv shell
exit
```


### 1. pyenv (version management) 

- [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)

```shell

# Install pyenv 

## (linux / mac os)
curl https://pyenv.run | bash

## (windows)
https://github.com/pyenv-win/pyenv-win

# Check the available versions
pyenv install --list

# Install a specific version
pyenv install 3.8.0

# Set the global version
pyenv global 3.8.0

# Set the local version
pyenv local 3.8.0

# Set the shell version
pyenv shell 3.8.0

# Uninstall a version
pyenv uninstall 3.8.0

# List all installed versions
pyenv versions

# List all versions
pyenv versions --all

# List all versions with the path
pyenv prefix

```

### 2. pipenv (package management)

```shell

# Install pipenv
pip install pipenv

# Create a new environment
pipenv --python 3.8.0

# Install a package
pipenv install requests

# Install a package with a specific version
pipenv install requests==2.25.1

# Install a package with a specific version range
pipenv install "requests>=2.25.1"

# Install a package with a specific version range
pipenv install "requests>=2.25.1,<2.26.0"

# Install a package from a requirements file
pipenv install -r requirements.txt

# Uninstall a package
pipenv uninstall requests

# List all installed packages
pipenv graph

# Run a command in the virtual environment
pipenv run python -c "import requests; print(requests.__version__)"

# Activate the virtual environment
pipenv shell

# Deactivate the virtual environment
exit

```


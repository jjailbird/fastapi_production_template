# Python

## Python Version and Package management

### 0. Summary

```shell

# Install python version management
pyenv versions
pyenv install --list
pyenv install 3.8.0

# Generate Profile
pipenv --python 3.8.0
pipenv install [package_name]
pipenv install -r requirements.txt
pipenv install -r requirements.txt --dev

# Using Profile
pipenv install # from Pipfile
pipenv graph # list all installed packages
pipenv shell # activate the virtual environment
exit
```


### 1. pyenv (version management) 

- [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)

```shell

# Install pyenv 

## (linux / mac os)
sudo apt update && sudo apt install -y build-essential curl libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
curl https://pyenv.run | bash

## (add below scripts to .bashrc or .zshrc)
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"

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
pipenv install requests --dev

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
pipenv uninstall --all

# List all installed packages
pipenv graph

# Run a command in the virtual environment
pipenv run python -c "import requests; print(requests.__version__)"

# Activate the virtual environment
pipenv shell

# Deactivate the virtual environment
exit


# Install from Pipfile and generate Pipfile.lock
pipenv install

# After edit Pipfile and apply Pipfile.lock
pipenv lock # Generate or update Pipfile.lock from Pipfile
pipenv sync # install only main packages from Pipfile.lock
pipenv sync --dev # install include dev packages from Pipfile.lock


# Change the python version

# 1. Remove the old environment
pipenv --rm

# 2. Change the python version in the Pipfile
sed -i "s/python_version = \".*\"/python_version = \"3.10.9\"/g" Pipfile

# 3. Create a new environment
pipenv install

```


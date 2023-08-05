# Wasd3r Python SDK

# Installing SDK

## Unix/macOS

```sh
python -m pip install wasd3r-sdk
```

## Windows

```sh
py -m pip install wasd3r-sdk
```

## Using specific blockchain locally (optional)

### Supporting [APTOS](https://aptos.dev/)

To use APTOS without a wasd3r server, [aptos-sdk](https://aptos.dev/sdks/python-sdk) needs to be installed optionally.

#### Unix/macOS

```sh
python -m pip install wasd3r-sdk[APTOS]
```

#### Windows

```sh
py -m pip install wasd3r-sdk[APTOS]
```

# Preparing DEV environment

## Using `pyenv`

[pyenv](https://github.com/pyenv/pyenv) could be installed via [this link](https://github.com/pyenv/pyenv#installation).

### Initialize env

```sh
pyenv install 3.8.13
pyenv global 3.8.13
git clone git@github.com:WASD3Rplay/wasd3r-sdk.git
cd wasd3r-sdk
PATH=$(pyenv root)/shims:$PATH; poetry env use python3.8; poetry install
```

### Start env

```sh
cd wasd3r-sdk
poetry shell

python --version
# Python 3.8.13

which python | xargs ls -al
# /poetry/virtualenvs/wasd3r-sdk-xx-py3.8/bin/python -> /pyenv/versions/3.8.13/bin/python3.8
```

## Using `Miniconda`

[Miniconda](https://docs.conda.io/projects/conda/en/stable/glossary.html#miniconda) could be install via [this link](https://docs.conda.io/en/latest/miniconda.html).

### Initialize env

```sh
conda create -n wasd3r-sdk-py3.8 python=3.8
conda activate wasd3r-sdk-py3.8
git clone git@github.com:WASD3Rplay/wasd3r-sdk.git
cd wasd3r-sdk
poetry env use python3.8; poetry install
```

### Start env

```sh
cd wasd3r-sdk
poetry shell

python --version
# Python 3.8.x

which python | xargs ls -al
# /poetry/virtualenvs/wasd3r-sdk-xx-py3.8/bin/python -> /miniconda/envs/wasd3r-sdk-py3.8/bin/python3.8
```

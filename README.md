# example-dvc-dataset

This repository contains example on how to restructure dataset as code utilizing Git and DVC

Directory structure

```shell
├── README.md
├── dataset
│   └── iris.csv
├── example_dvc_dataset
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   └── interface.cpython-38.pyc
│   └── interface.py
├── example_main.py
├── poetry.lock
└── pyproject.toml
```

- `dataset` dir contains the original dataset files which will be converted to DVC hash files

  - Note that, on the repository, only the `.dvc` file that exists, this is because the original dataset files will be uploaded to another storage. You can easily retrieve it using `dvc pull` command

- `example_dvc_dataset` will be the python package to programmatically accessing the dataset
- `example_main.py` is the example how to access the dataset from another script. E.g. training script
- `pyproject.toml` and `poetry.lock` is the files required by [Poetry](https://python-poetry.org/docs/) to manage and install all the dependencies

To start using this repo, don't forget to install all of the dependencies first

```shell
poetry install
```

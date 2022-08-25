# Supervised Learning in Action

The main purpose of this app is to showcase a sample application
using supervised learning techniques to train and validate a 
model for classifying images from dogs and cats

## Requirements

- Python 3.8.X
- Poetry: for instructions see https://python-poetry.org/docs/

## Installation

1. Verify Python and Poetry installation

    ```bash
    $ cd supervised-learning-in-action
    $ poetry env info
    # you should get a similar output
    Virtualenv
    Python:         3.2.12
    Implementation: CPython
    Path:           NA

    System
    Platform: darwin
    OS:       posix
    Python:   /path/to/python/3.7.12
    ```

2. Create virtual environment and install dependencies:

    ```bash
    $ poetry install
    ```

## Research Codebase

The folder `./notebook` in the repo root dir contains the notebooks 
for exploring data + training/validating the model

## Classifier App

Before running the Classifier App, you need to:

- Once you have a trained model, copy it to `./src/app/model`
- Copy some of the images under `./notebook/data/unlabeled_test_data` to `./src/app/static/testdata`

To run the application:

```bash
$ poetry run flask run
```
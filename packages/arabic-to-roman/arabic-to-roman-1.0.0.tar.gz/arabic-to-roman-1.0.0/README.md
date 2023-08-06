# Arabic number to Roman numeral converter

A simple converter that converts an Arabic number (e.g. `42`) to a Roman numeral (e.g. `XLII`).

Requires [Poetry](https://python-poetry.org/) to install:

```sh
poetry install --no-dev
```

## Running the tests

The tests consist of:

* Unit tests using `pytest`
* Static type checking using `mypy`

To run the tests, first install the required packages using

```sh
poetry install
```

Then run the tests with

```sh
poetry run test
```

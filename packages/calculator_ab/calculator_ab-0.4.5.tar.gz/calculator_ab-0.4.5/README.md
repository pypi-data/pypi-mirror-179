# Calculator

> Perform basic math operations

[![PyPI Version][pypi-image]][pypi-url]


`Calculator` performs:
 - addition
 - subraction
 - multiplication
 - division
 - n root of a number

## Installation

```sh
pip install calculator_ab
```

## Usage

Initializing the Calculator:
```python
>>> import calculator_ab
>>> calculator = Calculator()
```

An example of adding the number:
```python
>>> calculator.add(5)
```

An example of subtraction:
```python
>>> calculator.subtract(4)
```

An example of multiplication:
```python
>>> calculator.multiply(2)
```

An example of division:
```python
>>> calculator.divide(3)
```

An example of n root:
```python
>>> calculator.n_root(2)
```

Reseting the memory:
```python
>>> calculator.reset()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Make sure to add or update tests as appropriate.

Use [Black](https://black.readthedocs.io/en/stable/) for code formatting and [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/) for commit messages.

## [Changelog](CHANGELOG.md)

## License

[MIT](https://choosealicense.com/licenses/mit/)

<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/podsearch
[pypi-url]: https://pypi.org/project/calculator_ab/

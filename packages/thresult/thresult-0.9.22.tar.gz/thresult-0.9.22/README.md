[![Build][build-image]]()
[![Status][status-image]][pypi-project-url]
[![Stable Version][stable-ver-image]][pypi-project-url]
[![Coverage][coverage-image]]()
[![Python][python-ver-image]][pypi-project-url]
[![License][bsd3-image]][bsd3-url]


# thresult

## Overview

*Python* `Result` library for handling returned values (`Result`, `Ok`, `Err`) from functions/methods and handling errors. It is *error handling* library which is alternative to `try/except` style of programming.

It is inspired by great *Rust* `Result`, `Ok`, `Err` types.


## Installation

```bash
pip install thresult
```


## Simple Usage

### Traditional `try-except` example

```python
def div(x: float, y: float) -> float:
    z: float = x / y
    return z


z0: float = div(1.0, 2.0) # 0.5
z1: float = div(1.0, 0.0) # raises "ZeroDivisionError: division by zero" exception
```


### Unwrapping `Result` as Context Manager

```python
from thresult import Result


@Result
def div(x: float, y: float) -> float:
    z: float = x / y
    return z


try:
    with div(1.0, 0.0) as z:
        # unreachable
        r: float = z
except ZeroDivisionError as e:
    # exception happened
    pass
```


### Unwrapping `Result` in `unwrap` Context Manager

```python
from thresult import Result, unwrap


@Result
def f(x: float, y: float) -> float:
    z: float = x / y
    return z


try:
    with unwrap():
        # unreachable
        r: float = f(1, 0)
except ZeroDivisionError as e:
    # exception happened
    raise e
```


### Pattern-matching `Result` using `match-case`
```python
from thresult import Result, Ok, Err


@Result
def div(x: float, y: float) -> float:
    # can raise "ZeroDivisionError: division by zero" exception
    z: float = x / y
    return z


r: Result = div(1.0, 2.0) # Ok[float](0.5)

match r:
    case Ok(v):
        assert v == 0.5
    case Err(e):
        # unreachable
        # "ZeroDivisionError: division by zero"
        assert isinstance(e, ZeroDivisionError)
```

### In-place pattern-matching `Result` using `walrus operator` and `match-case`

```python
@Result
    def div(x: float, y: float) -> float:
        # can raise "ZeroDivisionError: division by zero" exception
        z: float = x / y
        return z


    match r := div(1.0, 2.0): # Ok[float](0.5)
        case Ok(v):
            assert v == 0.5
        case Err(e):
            # unreachable
            # "ZeroDivisionError: division by zero"
            assert isinstance(e, ZeroDivisionError)
```

## Advanced Usage


### Unwrapping `Result[float, ZeroDivisionError]` as Context Manager

```python
from thresult import Result, Ok, Err


@Result[float, ZeroDivisionError]
def div(x: float, y: float) -> float:
    z: float = x / y
    return z


try:
    with div(1.0, 0.0) as z:
        # unreachable 
        pass
except ZeroDivisionError as e:
    # exception happened
    pass
```


### Manually create Result value, and Structural Pattern Matching

```python
from thresult import Result, Ok, Err


def div(x: float, y: float) -> Result[float, ZeroDivisionError]:
    res: Result[float, ZeroDivisionError]

    try:
        # can raise "ZeroDivisionError: division by zero" exception
        z: float = x / y
        res = Ok[float](z)
    except ZeroDivisionError as e:
        res = Err[ZeroDivisionError](e)

    return res


r0: Result = div(1.0, 2.0) # Ok
r1: Result = div(1.0, 0.0) # Err

match r0:
    case Ok(v):
        print('Ok, value:', v)
    case Err(e):
        print('Err, error:', e) # "ZeroDivisionError: division by zero"

match r1:
    case Ok(v):
        print('Ok, value:', v)
    case Err(e):
        print('Err, error:', e) # "ZeroDivisionError: division by zero"

z0: float = r0.unwrap() # 0.5
z1: float = r1.unwrap_or(float('inf')) # inf
z1: float = r1.unwrap() # raises "ZeroDivisionError: division by zero" exception
```


### Decorate function with Result, and Structural Pattern Matching

```python
from thresult import Result, Ok, Err


@Result[float, ZeroDivisionError]
def div(x: float, y: float) -> float:
    # can raise "ZeroDivisionError: division by zero" exception
    z: float = x / y
    return z


r0: Result = div(1.0, 2.0) # Ok
r1: Result = div(1.0, 0.0) # Err

match r0:
    case Ok(v):
        print('Ok, value:', v)
    case Err(e):
        print('Err, error:', e) # "ZeroDivisionError: division by zero"

match r1:
    case Ok(v):
        print('Ok, value:', v)
    case Err(e):
        print('Err, error:', e) # "ZeroDivisionError: division by zero"

z0: float = r0.unwrap() # 0.5
z1: float = r1.unwrap_or(float('inf')) # inf
z1: float = r1.unwrap() # raises "ZeroDivisionError: division by zero" exception
```


## Run / Develop Cycle
```bash
docker run --rm -it -v $PWD/thresult:/code -w /code python:3.11-alpine python -B result.py
```


## Testing

```bash
docker-compose build thresult-test ; docker-compose run --rm -v $PWD:/test thresult-test
```


## Coverage

```bash
docker-compose build thresult-coverage ; docker-compose run --rm -v $PWD:/test thresult-coverage
```


## Building

```bash
docker-compose build thresult-build ; docker-compose run --rm thresult-build
```


## Licensing

`thresult` is licensed under the BSD 3 license.

Check the [LICENSE](https://opensource.org/licenses/BSD-3-Clause) for details


<!-- Badges -->
[bsd3-image]: https://img.shields.io/badge/License-BSD_3--Clause-blue.svg
[bsd3-url]: https://opensource.org/licenses/BSD-3-Clause
[build-image]: https://img.shields.io/gitlab/pipeline-status/tangledlabs/thresult?branch=main
[coverage-image]: https://img.shields.io/gitlab/pipeline-coverage/tangledlabs/thresult?branch=main

[pypi-project-url]: https://pypi.org/project/thresult/
[stable-ver-image]: https://img.shields.io/pypi/v/thresult?label=stable
[python-ver-image]: https://img.shields.io/pypi/pyversions/thresult.svg?logo=python&logoColor=FBE072
[status-image]: https://img.shields.io/pypi/status/thresult.svg

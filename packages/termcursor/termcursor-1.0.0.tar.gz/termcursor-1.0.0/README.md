[![Generic badge](https://img.shields.io/badge/Version-1.0.0-blue)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Python-%3E%3D3.10-blue)](https://shields.io/)

# termcursor

Hiding or showing the console cursor on Windows and Unix platforms with the Python Standard Library only

## Quickstart

### Requirements

This module use Python Standard Library only. Python version should be higher than *3.10*

### Install

```
pip install termcursor
```

### How to Use

This code works as module not a script.

#### Module level import

```
import termcursor

# hiding the console cursor
termcursor.hidecursor()

# showing the console cursor
termcursor.showcursor()
```

#### Function level import

```
from termcursor import hidecursor, showcursor

# hiding the console cursor
hidecursor()

# showing the console cursor
showcursor()
```

#### Help

```
import termcursor

help(termcursor)
```

### Examples

#### Module level import

Example is available in the [example.py](https://github.com/richardvecsey/termcursor/blob/main/example.py)

#### Function level import

Example is available in the [example2.py](https://github.com/richardvecsey/termcursor/blob/main/example2.py)

## License

The content of this repository is licensed under *MIT license*. For more details, check [LICENSE](https://github.com/richardvecsey/termcursor/blob/main/LICENSE)

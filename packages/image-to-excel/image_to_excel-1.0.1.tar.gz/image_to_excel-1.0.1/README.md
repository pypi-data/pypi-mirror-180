# image-to-excel

A simple project to convert from an image to an excel file, because my brother wanted something that did this.

## Installation

To install the project you only need to clone the repo and run pip install within the repo folder:

```bash
pip install .
```

If you like using virtual environments, you can easily install the project within one using [pipx](https://pypa.github.io/pipx/):

```bash
pipx install .
```

## Usage

You can use image-to-excel as an importable module:

```py
from image_to_excel import BaseClass
from pathlib import Path

app = BaseClass("config.yml")

app.image_to_excel(
    Path("input.jpg"), 100, Path("output.xlsx")
)
```

Or as a command line interface:

```bash
$ python3 -m image_to_excel
# or
$ image_to_excel -w 100 input.jpg output.xslx
```

## Documentation

Documentation for image-to-excel can be found within the docs folder.

# image-to-excel

A simple project to convert from an image to an excel file, because my brother wanted something that did this.

## Installation

You can install the project using pip :)

```bash
pip install image-to-excel
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
$ image-to-excel -w 100 input.jpg output.xslx
```

## Documentation

Documentation for image-to-excel can be found within the docs folder.

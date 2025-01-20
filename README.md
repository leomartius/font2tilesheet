# ASCII Tilesheet Generator

This script generates an ASCII tilesheet image from a BDF font file. It
converts the BDF font to a PIL-readable format and uses it to create a
tilesheet containing all printable ASCII characters.


## Features

- Generates a tilesheet containing ASCII characters (from `0x20` to `0x7E`).
- Configurable number of columns in the tilesheet.
- Option to display the generated tilesheet.


## Requirements

- Python 3.13
- [Pillow](https://pypi.org/project/pillow/) library


## Usage

```
usage: font2tilesheet.py [-h] [--cols COLS] [--show] FONT

Generate an ASCII tilesheet from a BDF font.

positional arguments:
  FONT         path to the BDF font file

options:
  -h, --help   show this help message and exit
  --cols COLS  number of columns in the tilesheet (default: 16)
  --show       display the generated image
```


## Output

The script saves the generated tilesheet as a `.png` file with the same name
as the input BDF file.


## Licensing

This is free and unencumbered software released into the public domain. See
LICENSE for details.

# Reading CSV Data

## Introduction

This lesson starts the chapter by reading a CSV file. The file holds the daily weather for Sitka,
Alaska, for July 2021. Each row is one day, and each column is one measurement. The first row is a
header that names the columns.

Python's `csv` module reads the rows for us. The data file is in the `data` folder beside the lesson
scripts. The lesson uses a helper module, `relative_paths.py`, to find the file no matter where you run
the script from.

---

## The Code

The lessons in this chapter use a helper module, `relative_paths.py`, to build paths to the data files:

```python
"""A module to expose a simple method to interact with files via relative path"""

from os import path

ROOT_DIR = None

def get_path(file_name: str, folder: str=None, parent_levels: int=0, debug: bool=False) -> str:
    """Returns a relative path to a specified file"""
    initialize(debug)
    for _ in range(parent_levels):
        file_name = path.join("..", file_name)
    file_path = path.join(ROOT_DIR, file_name) if folder is None \
        else path.join(ROOT_DIR, folder, file_name)
    if debug:
        print(f"Set file path: {file_path}")
    return file_path

def initialize(debug: bool) -> None:
    """Store the root directory"""
    global ROOT_DIR
    if ROOT_DIR is not None:
        return
    ROOT_DIR = path.dirname(__file__)
    if debug:
        print(f"Set root directory: {ROOT_DIR}")
```

The lesson script:

```python
"""Lesson 1.1 - Reading CSV Data"""

# Add this library to access CSV parsing methods
import csv
from pathlib import Path
from relative_paths import get_path


folder = "data"
# This file contains the temperatures for Sitka, AK for July 2021
file_name = "sitka_weather_07-2021_simple.csv"
file_path = get_path(file_name, folder)

csv_file = Path(file_path)
lines = csv_file.read_text(encoding="UTF-8").splitlines()

# Create a CSV Reader
reader = csv.reader(lines)

# Read the header row to obtain the labels for the data in the rest of the CSV
#     and advance the cursor
header_row = next(reader)

# Note the column positions of the significant data
# • Date is in column 2
# • High is in column 4
# • Low is in column 5

print(header_row)
```

---

### Walking Through the Code

**Finding the file.** `get_path()` returns the full path to a file in the `data` folder. It works from
the location of the helper module, so the script finds the data wherever you run it from.

**Reading the file.** `read_text()` loads the whole file, and `splitlines()` turns it into a list of
lines. `csv.reader()` then reads each line as a list of values.

**The header row.** `next(reader)` reads the first line, which holds the column names, and moves the
reader on to the data rows. The comments note where the useful columns are: the date in column 2, the
high in column 4, and the low in column 5.

**Printing the header.** `print(header_row)` shows the column names as a list, which is the first check
that the file has been read correctly.

---

### Output

The terminal prints the header row as a list of column names:

```
['STATION', 'NAME', 'DATE', 'TAVG', 'TMAX', 'TMIN']
```

---

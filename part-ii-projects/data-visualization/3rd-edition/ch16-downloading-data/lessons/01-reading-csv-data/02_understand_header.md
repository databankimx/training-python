# Understanding the Header Row

## Introduction

The header row tells us what each column holds, but the names alone don't tell us which position is
which. This lesson prints each name next to its position, so we know which index to use when we
extract the data.

---

## The Code

```python
"""Lesson 1.2 - Understanding the Header Row"""

import csv
from pathlib import Path
from relative_paths import get_path

folder = "data"
file_name = "sitka_weather_07-2021_simple.csv"
file_path = get_path(file_name, folder)

csv_file = Path(file_path)
lines = csv_file.read_text(encoding="UTF-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# The enumerate() function provides the index and value of each item in a list
# We'll use this to view what the headers and their indices are
# We can later use this for parsing the CSV data
for index, column in enumerate(header_row):
    print(index, column)
```

---

### Walking Through the Code

**Reading the header.** The first few lines are the same as in the last lesson: find the file, read it,
and take the header row.

**Numbering the columns.** `enumerate()` gives each column its index along with its name. The loop prints
one pair per line.

**Using the indexes later.** Once we know that the high temperature is at index 4, we can use `row[4]` to
read it from every data row.

---

### Output

The terminal prints each column's index and name, one per line:

```
0 STATION
1 NAME
2 DATE
3 TAVG
4 TMAX
5 TMIN
```

---

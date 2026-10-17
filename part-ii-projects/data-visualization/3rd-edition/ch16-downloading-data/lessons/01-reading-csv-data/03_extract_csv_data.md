# Extracting CSV Data

## Introduction

Now that we know the high temperature is in column 4, we can pull that value from every row of the
file. This lesson extracts the highs into a list of numbers, which is the first step towards plotting
them.

---

## The Code

```python
"""Lesson 1.3 - Extracting CSV Data"""

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

# for index, column in enumerate(header_row):
#     print(index, column)

# Now that we know tha the high temperature (TMAX) is in index 4,
#    we can extract the data from the CSV rows
highs = [int(row[4]) for row in reader]

print(highs)
```

---

### Walking Through the Code

**Reading the rows.** `reader` is positioned after the header, so the list comprehension sees only the
data rows.

**Extracting the highs.** `row[4]` is the high temperature in each row. `int()` converts the text to a
number, and the comprehension collects the results into `highs`.

**Printing the list.** `print(highs)` shows the list, so you can check its length and values.

---

### Output

The terminal prints the list of daily high temperatures for July 2021:

```
[61, 60, 66, 60, 65, 59, 58, 58, 57, 60, 60, 60, 57, 58, 60, 61, 63, 63, 70, 64, 59, 63, 61, 58, 59, 64, 62, 70, 70, 73, 66]
```

---

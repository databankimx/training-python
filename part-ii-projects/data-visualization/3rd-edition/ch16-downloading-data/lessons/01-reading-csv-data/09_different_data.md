# Different Data

## Introduction

Not every weather file has the same layout. The Death Valley file has its columns in different positions
from the Sitka file, so the same code would read the wrong values. This lesson shows how to spot that
difference by printing the header row again.

---

## The Code

```python
"""Lesson 1.9 - Different Data"""

from pathlib import Path
import csv
from relative_paths import get_path

folder = "data"
# This file contains the temperatures for Death Valley for 2021
file_name = "death_valley_2021_simple.csv"
file_path = get_path(file_name, folder)

csv_file = Path(file_path)
lines = csv_file.read_text(encoding="UTF-8").splitlines()

# Create a CSV Reader
reader = csv.reader(lines)

# Read the header row to obtain the labels for the data in the rest of the
#     CSV and advance the cursor
header_row = next(reader)

# Often, when you work with data, the structure of one data file may differ
#     from that of another
# Note the differences in the Death Valley header row
# • Date is in column 2
# • High is in column 3
# • Low is in column 4

print(header_row)
```

---

### Walking Through the Code

**The same steps.** The script opens the file and reads the header row, just as in the Sitka lessons.

**Different positions.** The comments show the Death Valley layout: the high is in column 3 and the low in
column 4, one place earlier than in the Sitka file. Code written for one file won't work on the other
without changes.

---

### Output

The terminal prints the Death Valley header row as a list of column names:

```
['STATION', 'NAME', 'DATE', 'TMAX', 'TMIN', 'TOBS']
```

---

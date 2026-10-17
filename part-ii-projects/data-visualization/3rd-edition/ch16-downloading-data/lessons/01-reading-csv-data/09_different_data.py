"""Lesson 1.9 - Different Data"""

from pathlib import Path
import csv
from relative_paths import get_path

folder = "Data"
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

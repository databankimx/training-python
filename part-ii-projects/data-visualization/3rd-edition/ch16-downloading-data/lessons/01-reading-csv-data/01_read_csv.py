"""Lesson 1.1 - Reading CSV Data"""

# Add this library to access CSV parsing methods
import csv
from pathlib import Path
from relative_paths import get_path


folder = "Data"
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

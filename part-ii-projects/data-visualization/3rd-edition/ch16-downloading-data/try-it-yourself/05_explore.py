"""Assignment 16.05"""

# Explore: Generate a few more visualizations that examine any other weather
#          aspect you're interested in for any locations you're curious about.

from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from relative_paths import get_path

folder = "data"
file_name = "lewisville_weather_2023_jan_to_sep.csv"
file_path = get_path(file_name, folder)

csv_file = Path(file_path)
lines = csv_file.read_text(encoding="UTF-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# The daily temperature range is the gap between the high and the low for each day
dates, ranges = [], []
for row in reader:
    row_date = datetime.strptime(row[0], "%m/%d/%Y")
    try:
        high = float(row[1])
        low = float(row[2])
    except ValueError:
        print(f"Missing data for {row_date}")
    else:
        dates.append(row_date)
        ranges.append(high - low)

# Show each day's range as a bar, so the spread of the days is easy to compare
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.bar(dates, ranges, color="orange", width=1.0)
ax.set_title("Lewisville, TX - Daily Temperature Range, Jan-Sep 2023", fontsize=14)
ax.set_xlabel("", fontsize=8)
ax.set_ylabel("Range (F)", fontsize=14)
ax.tick_params(labelsize=8)
fig.autofmt_xdate()

plt.show()

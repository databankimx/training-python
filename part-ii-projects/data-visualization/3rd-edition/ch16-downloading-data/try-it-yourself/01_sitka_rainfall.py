"""Assignment 16.1"""

# Sitka Rainfall: Sitka is in a temperate rainforest, so it gets a fair amount of rainfall.
#                 In the data file sitka_weather_2018_simple.csv is a header called PRCP, which
#                 represents daily rainfall amounts. Make a visualization focusing on the data
#                 in this column. You can repeat the exercise for Death Valley if you're curious
#                 how little rainfall occurs in a desert.

from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from relative_paths import get_path

folder = "Data"
file_name = "sitka_weather_2021_full.csv"
file_path = get_path(file_name, folder)

csv_file = Path(file_path)
lines = csv_file.read_text(encoding="UTF-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, prec = [], []
for row in reader:
    row_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        rain = float(row[5])
    except ValueError:
        print(f"Missing data for {row_date}")
    else:
        dates.append(row_date)
        prec.append(rain)

# Create the plot
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()

# Add plot for rain
ax.plot(dates, prec, color="blue")
# Format the plot
ax.set_title("Sitka, AK - Daily Precipitation, 2021", fontsize=18)
ax.set_xlabel("", fontsize=8)
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.tick_params(labelsize=8)

# Add date formatting
fig.autofmt_xdate()
fig.canvas.manager.set_window_title("Sitka, AK - Daily Precipitation")

plt.show()

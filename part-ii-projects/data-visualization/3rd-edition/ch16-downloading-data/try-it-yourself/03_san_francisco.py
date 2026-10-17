"""Assignment 16.3"""

# San Francisco: Are temperatures in San Francisco more like temperatures in Sitka or temperatures in
#                Death Valley? Download some data for San Francisco, and generate a high-low temperature
#                plot for San Francisco to make a comparison.

from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from relative_paths import get_path

folder = "Data"
file_name = "san_francisco_weather_2023_jan_to_sep.csv"
file_path = get_path(file_name, folder)

csv_file = Path(file_path)
lines = csv_file.read_text(encoding="UTF-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows = [], [], []
for row in reader:
    row_date = datetime.strptime(row[0], "%m/%d/%Y")
    try:
        high = float(row[1])
        low = float(row[2])
    except ValueError:
        print(f"Missing data for {row_date}")
    else:
        # Only append when we have all data for the day
        dates.append(row_date)
        highs.append(high)
        lows.append(low)

# Create the plot
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()

# Add plots for both high and low temperatures (alpha is opacity)
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)

# Add shading between the high/low plots (alpha is opacity)
ax.fill_between(dates, highs, lows, facecolor="green", alpha=0.1)

# Format the plot
ax.set_title("San Francisco, CA - Daily High & Low Temperatures, Jan-Sep 2023", fontsize=14)
ax.set_xlabel("", fontsize=8)
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.tick_params(labelsize=8)

# Add date formatting
fig.autofmt_xdate()
fig.canvas.manager.set_window_title("San Francisco, CA Weather")

plt.show()

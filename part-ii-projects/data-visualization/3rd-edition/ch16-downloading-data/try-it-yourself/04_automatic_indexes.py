"""Assignment 16.4"""

# Automatic Indexes: In this section, we hardcoded the indexes corresponding to
#                    the TMIN and TMAX columns. Use the header row to determine
#                    the indexes for these values, so your program can work for
#                    Sitka or Death Valley. Use the station name to automatically
#                    generate an appropriate title for your graph as well.

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

station_index = header_row.index("STATION")
station = None
name_index = header_row.index("NAME")
name = None

date_index = header_row.index("DATE")
high_index = header_row.index("TMAX")
low_index = header_row.index("TMIN")

dates, highs, lows = [], [], []
for row in reader:
    if station is None:
        station = row[station_index]
    if name is None:
        name = row[name_index]

    row_date = datetime.strptime(row[date_index], "%Y-%m-%d")

    try:
        high = float(row[high_index])
        low = float(row[low_index])
    except ValueError:
        print(f"Missing data for {row_date}")
    else:
        dates.append(row_date)
        highs.append(high)
        lows.append(low)

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs,color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, lows, highs, color="green", alpha=0.1)
ax.set_title(f"Daily High & Low Temp, 2021\nStation: {station} - {name}", fontsize=14)
ax.set_xlabel("", fontsize=8)
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.tick_params(labelsize=8)
fig.autofmt_xdate()
fig.canvas.manager.set_window_title(f"{name} Weather")

plt.show()

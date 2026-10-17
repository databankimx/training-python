"""Lesson 1.4 - Plotting the Temperatures"""

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from relative_paths import get_path

folder = "Data"
file_name = "sitka_weather_07-2021_simple.csv"
file_path = get_path(file_name, folder)

csv_file = Path(file_path)
lines = csv_file.read_text(encoding="UTF-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index, column in enumerate(header_row):
#     print(index, column)

# Now that we know tha the high temperature (TMAX) is in index 4,
#     we can extract the data from the CSV rows
highs = [int(row[4]) for row in reader]

# Plot the high temperatures
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(highs, color="red")

# Format the plot
ax.set_title("Sitka, AK - Daily High Temperatures, July 2021", fontsize=18)
# We're intentionally leaving the x-axis labels blank, because later we'll fill in the dates
ax.set_xlabel("", fontsize=14)
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()

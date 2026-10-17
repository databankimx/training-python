"""Assignment 16.4"""
# Automatic Indexes: In this section, we hardcoded the indexes corresponding to the
#                    TMIN and TMAX columns. Use the header row to determine the indexes
#                    for these values, so your program can work for Sitka or Death
#                    Valley. Use the station name to automatically generate an appropriate
#                    title for your graph as well.

from datetime import datetime
import os
import csv
import matplotlib.pyplot as plt
import numpy as np

data_file_names = {
    "1": "sitka_weather_2018_simple",
    "2": "death_valley_2018_simple",
    "3": "san_francisco_2018",
}

resp = "0"
while resp not in list(data_file_names):
    for val in range(1, len(data_file_names) + 1):
        print(f"{val} : {data_file_names[f'{val}']}")
    resp = input("Select a file to process:\n> ")
    if resp not in list(data_file_names):
        print("Invalid selection!")

ROOT_DIR = os.path.dirname(__file__)
data_file = os.path.join(ROOT_DIR, "Data", f"{data_file_names[resp]}.csv")

print(f"Processing file: {data_file}")

S_LABEL = "STATION"
N_LABEL = "NAME"
H_LABEL = "TMAX"
L_LABEL = "TMIN"
D_LABEL = "DATE"

L_COLOR = "#1D2E68"
H_COLOR = "#F9423A"
F_COLOR = "#008013"

with open(data_file, encoding="UTF-8") as f:
    reader = csv.reader(f)
    header_row = next(reader)
    h_pos = header_row.index(H_LABEL)
    l_pos = header_row.index(L_LABEL)
    d_pos = header_row.index(D_LABEL)
    s_pos = header_row.index(S_LABEL)
    n_pos = header_row.index(N_LABEL)

    station, name = "", ""

    dates, highs, lows = [], [], []
    for row in reader:
        if station == "":
            station = row[s_pos]
        if name == "":
            name = row[n_pos]

        date = datetime.strptime(row[d_pos], "%Y-%m-%d")
        try:
            high = int(row[h_pos])
            low = int(row[l_pos])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c = L_COLOR, alpha = 0.5)
    ax.plot(dates, highs, c = H_COLOR, alpha = 0.5)
    ax.fill_between(dates, highs, lows, facecolor = F_COLOR, alpha = 0.1)
    ax.set_title(f"Daily High & Low Temp - 2018\n{name} - [{station}]", fontsize = 14)
    ax.set_xlabel("", fontsize = 16)
    ax.set_ylabel("Temperature (F)", fontsize = 16)
    fig.autofmt_xdate()
    ax.tick_params(axis ="both", which ="major", labelsize = 12)
    min_temp = min(lows) - min(lows) % 5
    max_temp = max(highs) + max(highs) % 5
    ax.set_yticks(np.arange(min_temp, max_temp, 5))

    plt.show()

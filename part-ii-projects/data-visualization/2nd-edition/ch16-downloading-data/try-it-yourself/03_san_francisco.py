"""Assignment 16.3"""
# San Francisco: Are temperatures in San Francisco more like temperatures in Sitka
#                or temperatures in Death Valley? Download some data for San Francisco,
#                and generate a high-low temperature plot for San Francisco to make
#                a comparison.

from datetime import datetime
import os
import csv
import matplotlib.pyplot as plt
import numpy as np

ROOT_DIR = os.path.dirname(__file__)
data_file = os.path.join(ROOT_DIR, "Data", "san_francisco_2018.csv")

h_label = "TMAX"
l_label = "TMIN"
d_label = "DATE"
L_COLOR = "#A020F0"
H_COLOR = "#BB4A00"
F_COLOR = "#A020F0"

with open(data_file, encoding="UTF-8") as f:
    reader = csv.reader(f)
    header_row = next(reader)
    h_pos = header_row.index(h_label)
    l_pos = header_row.index(l_label)
    d_pos = header_row.index(d_label)
    dates, highs, lows = [], [], []
    for row in reader:
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
    ax.set_title("Daily High & Low Temp - 2018\nSan Francisco, CA", fontsize = 20)
    ax.set_xlabel("", fontsize = 16)
    ax.set_ylabel("Temperature (F)", fontsize = 16)
    fig.autofmt_xdate()
    ax.tick_params(axis ="both", which ="major", labelsize = 12)
    min_temp = min(lows) - min(lows) % 5
    max_temp = max(highs) + max(highs) % 5
    ax.set_yticks(np.arange(min_temp, max_temp, 5))

    plt.show()

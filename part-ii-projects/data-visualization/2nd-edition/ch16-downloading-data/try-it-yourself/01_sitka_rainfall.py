"""Assignment 16.1"""
# Sitka Rainfall: Sitka is in a temperate rainforest, so it gets a fair amount of rainfall.
#                 In the data file sitka_weather_2018_simple.csv is a header called PRCP, which
#                 represents daily rainfall amounts. Make a visualization focusing on the data
#                 in this column. You can repeat the exercise for Death Valley if you're curious
#                 how little rainfall occurs in a desert.

from datetime import datetime
import os
import csv
import matplotlib.pyplot as plt
import numpy as np

ROOT_DIR = os.path.dirname(__file__)
data_file = os.path.join(ROOT_DIR, "Data", "sitka_weather_2018_simple.csv")

p_label = "PRCP"
d_label = "DATE"

with open(data_file, encoding="UTF-8") as f:
    reader = csv.reader(f)
    header_row = next(reader)
    p_pos = header_row.index(p_label)
    d_pos = header_row.index(d_label)
    dates, rainfall = [], []
    for row in reader:
        date = datetime.strptime(row[d_pos], "%Y-%m-%d")
        try:
            rain = float(row[p_pos])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            dates.append(date)
            rainfall.append(rain)

    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.plot(dates, rainfall, c="green", alpha=0.5)
    ax.set_title("Daily Rainfall - 2018\nSitka, AK", fontsize=20)
    ax.set_xlabel("", fontsize=16)
    ax.set_ylabel("Rainfall (in)", fontsize=16)
    fig.autofmt_xdate()
    ax.tick_params(axis="both", which="major", labelsize=12)
    ax.set_yticks(np.arange(0, max(rainfall) + 1, 0.5))

    plt.show()

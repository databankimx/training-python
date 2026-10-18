"""Assignment 16.5"""
# Explore: Generate a few more visualizations that examine any other weather aspect
#          you're interested in for any locations you're curious about.
from datetime import datetime
import os
import csv
import matplotlib.pyplot as plt

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "data", "north_texas_weather_2022_jan-jun.csv")

DALLAS = "USW00003971"

with open(file_path, encoding="UTF-8") as f:
    reader = csv.reader(f)
    header_row = next(reader)
    d_pos = header_row.index("DATE")
    p_pos = header_row.index("PRCP")
    dates, rainfall = [], []
    for row in reader:
        # Skip rows not from the Dallas NOAA station
        if row[0] != DALLAS:
            continue

        date = datetime.strptime(row[d_pos], "%Y-%m-%d")
        try:
            rain = float(row[p_pos])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            dates.append(date)
            rainfall.append(rain)

    # Rain falls in short bursts, so bars show each day's total clearly
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.bar(dates, rainfall, color="green", width=1.0)
    ax.set_title("Daily Rainfall - January to June 2022\nDallas, TX", fontsize=20)
    ax.set_xlabel("", fontsize=16)
    ax.set_ylabel("Rainfall (in)", fontsize=16)
    fig.autofmt_xdate()
    ax.tick_params(axis="both", which="major", labelsize=12)

    plt.show()

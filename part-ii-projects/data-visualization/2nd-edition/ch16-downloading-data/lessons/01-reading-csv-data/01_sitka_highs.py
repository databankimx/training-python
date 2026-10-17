"""Lesson 1.1 - Reading CSV Data"""

from datetime import datetime
import os
# The CSV module should not require installation
import csv
import matplotlib.pyplot as plt
import numpy as np

ROOT_DIR = os.path.dirname(__file__)
# file_path = os.path.join(ROOT_DIR, "Data", "sitka_weather_07-2018_simple.csv")
file_path = os.path.join(ROOT_DIR, "Data", "sitka_weather_2018_simple.csv")

with open(file_path, encoding="UTF-8") as f:
    # Open the CSV file
    reader = csv.reader(f)
    # Read the first line of the file (automatically parsing to a list)
    header_row = next(reader)

    # print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # Get high temperatures from file
    dates, highs = [], []
    # Note: We've already read the header, so we can read ALL the remaining rows
    for row in reader:
        # We'll use strptime() to parse and format dates
        dates.append(datetime.strptime(row[2], "%Y-%m-%d"))
        highs.append(int(row[5]))

    # The following format abbreviations are supported in strptime()
	# -------------------------------------------------
	#       Date/Time Formats
	# -------------------------------------------------
	# Argument         Meaning
	# -------------------------------------------------
	#   %A     Weekday name, such as Monday
	#   %B     Month name, such as January
	#   %m     Month, as a number (01 to 12)
	#   %d     Day of the month, as a number (01 to 31)
	#   %Y     Four-digit year, such as 2019
	#   %y     Two-digit year, such as 19
	#   %H     Hour, in 24-hour format (00 to 23)
	#   %I     Hour, in 12-hour format (01 to 12)
	#   %p     AM or PM
	#   %M     Minutes (00 to 59)
	#   %S     Seconds (00 to 61)
	# -------------------------------------------------

    # Plot the high temperatures.
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c = "red")

    # Format plot.
    # ax.set_title("Daily high temperatures, July 2018", fontsize = 24)
    ax.set_title("Sitka, AK - Daily high temperatures - 2018", fontsize = 24)
    ax.set_xlabel("", fontsize = 16)
    ax.set_ylabel("Temperature (F)", fontsize = 16)
    fig.autofmt_xdate()
    ax.tick_params(axis ="both", which ="major", labelsize = 12)
    ax.set_yticks(np.arange(min(highs) - min(highs) % 5, max(highs) + 5, 5))

    plt.show()

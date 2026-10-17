"""Try It Yourself: Download Your Own Data"""

# To obtain data, do the following:
#
# 1. Visit the NOAA Climate Data Online site at https://www.ncdc.noaa.gov/cdo-web/
#    In the Discover Data By section, click Search Tool. In the Select a Dataset box,
#    choose Daily Summaries.
#
# 2. Select a date range, and in the Search For section, choose ZIP Codes.
#    Enter the ZIP Code you're interested in, and click Search.
#
# 3. On the next page, you'll see a map and some information about the area you're
#    focusing on. Below the location name, click View Full Details, or click the map
#    and then click Full Details.
#
# 4. Scroll down and click Station List to see the weather stations that are available
#    in this area. Choose one of the stations, and click Add to Cart. This data is
#    free, even though the site uses a shopping cart icon. In the upper-right corner,
#    click the cart.
#
# 5. In Select the Output, choose Custom GHCN-Daily CSV. Make sure the date range
#    is correct, and click Continue.
#
# 6. On the next page, you can select the kinds of data you want. You can download
#    one kind of data, for example, focusing on air temperature, or you can download
#    all the data available from this station. Make your choices, and then click Continue.
#
# 7. On the last page, you'll see a summary of your order. Enter your email address,
#    and click Submit Order. You'll receive a confirmation that your order was received,
#    and in a few minutes you should receive another email with a link to download
#    your data.

from datetime import datetime
import os
import csv
import matplotlib.pyplot as plt
import numpy as np

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(
    ROOT_DIR, "Data", "north_texas_weather_2022_jan-jun.csv")

DALLAS = "USW00003971"

with open(file_path, encoding="UTF-8") as f:
    reader = csv.reader(f)
    header_row = next(reader)
    d_pos = header_row.index("DATE")
    h_pos = header_row.index("TMAX")
    l_pos = header_row.index("TMIN")
    p_pos = header_row.index("PRCP")
    dates, highs, lows, precip = [], [], [], []
    for row in reader:
        # Skip rows not from local NOAA station
        if row[0] != DALLAS:
            continue

        date = datetime.strptime(row[d_pos], "%Y-%m-%d")

        # Here, we will use a try-except-else block to address dates without data
        try:
            high = int(row[h_pos])
            low = int(row[l_pos])
            prec = float(row[p_pos])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)
            precip.append(prec)

    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c="red", alpha=0.5)
    ax.plot(dates, lows, c="blue", alpha=0.5)
    ax.plot(dates, precip, c="green", alpha=0.5)
    polygon = ax.fill_between(
        dates, highs, lows, facecolor="orange", alpha=0.1)

    ax.set_title(
        "Daily high and low temperatures (plus precip.) - 2022\nDallas, TX", fontsize=20)
    ax.set_xlabel("", fontsize=16)
    ax.set_ylabel("Temperature (F) & Precip (in)", fontsize=16)
    fig.autofmt_xdate()
    ax.tick_params(axis="both", which="major", labelsize=12)
    min_y = 0 if min(lows) > 0 else min(lows) - min(lows) % 5
    ax.set_yticks(np.arange(min_y, max(highs) + 5, 5))

    plt.show()

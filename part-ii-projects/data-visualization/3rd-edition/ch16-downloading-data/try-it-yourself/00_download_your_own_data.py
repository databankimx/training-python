"""Assignment 16.0 - Download Your Own Data"""

# pylint: disable=line-too-long

# To obtain data, do the following:
#
# 1. Visit the NOAA Climate Data Online site at https://www.ncdc.noaa.gov/cdo-web/
#    In the Discover Data By section, click Search Tool. In the Select a Dataset box, choose Daily Summaries.
#
# 2. Select a date range, and in the Search For section, choose ZIP Codes.
#    Enter the ZIP Code you're interested in, and click Search.
#
# 3. On the next page, you'll see a map and some information about the area you're focusing on.
#    Below the location name, click View Full Details, or click the map and then click Full Details.
#
# 4. Scroll down and click Station List to see the weather stations that are available in this area.
#    Choose one of the stations, and click Add to Cart. This data is free, even though the site uses a shopping cart icon.
#    In the upper-right corner, click the cart.
#
# 5. In Select the Output, choose Custom GHCN-Daily CSV. Make sure the date range is correct, and click Continue.
#
# 6. On the next page, you can select the kinds of data you want. You can download one kind of data, for example,
#    focusing on air temperature, or you can download all the data available from this station.
#    Make your choices, and then click Continue.
#
# 7. On the last page, you'll see a summary of your order. Enter your email address, and click Submit Order.
#    You'll receive a confirmation that your order was received, and in a few minutes you should receive another
#    email with a link to download your data.

# Below is an example plotting high/low temps for Lewisville, TX Jan-Sep 2023

# NOAA data was down on the date I extracted the data, so I got this example from here:
# https://open-meteo.com/en/docs/historical-weather-api#latitude=33.0462&longitude=-96.9942&start_date=2023-01-01&hourly=&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,precipitation_sum,rain_sum,snowfall_sum&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago

from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from relative_paths import get_path

folder = "Data"
file_name = "lewisville_weather_2023_jan_to_sep.csv"
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
ax.set_title(
    "Lewisville, TX - Daily High & Low Temperatures, Jan-Sep 2023", fontsize=14)
ax.set_xlabel("", fontsize=8)
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.tick_params(labelsize=8)

# Add date formatting
fig.autofmt_xdate()
fig.canvas.manager.set_window_title("Lewisville, TX Weather")

plt.show()

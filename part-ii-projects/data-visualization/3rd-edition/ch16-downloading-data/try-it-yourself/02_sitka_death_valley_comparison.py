"""Assignment 16.2"""

# Sitka–Death Valley Comparison: The temperature scales on the Sitka and Death Valley graphs reflect
#                                the different data ranges. To accurately compare the temperature range
#                                in Sitka to that of Death Valley, you need identical scales on the y-axis.
#                                Change the settings for the y-axis on one or both of the charts in Figures
#                                16-5 and 16-6. Then make a direct comparison between temperature ranges in
#                                Sitka and Death Valley (or any two places you want to compare).

from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from relative_paths import get_path

SH_COLOR = "red"
SL_COLOR = "blue"
DH_COLOR = "orange"
DL_COLOR = "green"

D_LABEL = "DATE"
H_LABEL = "TMAX"
L_LABEL = "TMIN"
labels = [D_LABEL, H_LABEL, L_LABEL]

increment_d = True

folder = "Data"
s_file = get_path("sitka_weather_2021_simple.csv", folder)
s_path = Path(s_file)
d_file = get_path("death_valley_2021_simple.csv", folder)
d_path = Path(d_file)

with s_path.open(encoding="utf-8") as sf, d_path.open(encoding="utf-8") as df:
    s_reader, d_reader = csv.reader(sf), csv.reader(df)
    s_header_row, d_header_row = next(s_reader), next(d_reader)

    sd_pos, sh_pos, sl_pos = [s_header_row.index(label) for label in labels]
    dd_pos, dh_pos, dl_pos = [d_header_row.index(label) for label in labels]

    dates, s_highs, s_lows, d_highs, d_lows = [], [], [], [], []

    while True:
        try:
            s_row = next(s_reader)
            d_row = next(d_reader)
        # pylint: disable=bare-except
        except:
            # If we have run out of rows in either file, stop
            break

        s_date = datetime.strptime(s_row[sd_pos], "%Y-%m-%d")
        d_date = datetime.strptime(d_row[dd_pos], "%Y-%m-%d")

        done = False

        # We only want to list dates that exist in both files
        while s_date != d_date:
            try:
                if s_date < d_date:
                    s_row = next(s_reader)
                else:
                    d_row = next(d_reader)
            # pylint: disable=bare-except
            except:
                # If we have run out of rows in either file, stop
                done = True
                break

        # If we have run out of rows in either file, stop
        if done:
            break

        try:
            # Get all high/low temps
            s_low = int(s_row[sl_pos])
            s_high = int(s_row[sh_pos])
            d_low = int(d_row[dl_pos])
            d_high = int(d_row[dh_pos])
        except ValueError:
            print(f"Missing data for {s_date}")
        else:
            # Only add to graph if everything had values
            dates.append(s_date)
            s_highs.append(s_high)
            s_lows.append(s_low)
            d_highs.append(d_high)
            d_lows.append(d_low)

    # Create the plot
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()

    # Add plots for all high and low temperatures
    ax.plot(dates, s_highs, color=SH_COLOR, alpha=0.5)
    ax.plot(dates, s_lows, color=SL_COLOR, alpha=0.5)
    ax.fill_between(dates, s_highs, s_lows, facecolor=SL_COLOR, alpha=0.1)
    ax.plot(dates, d_highs, color=DH_COLOR, alpha=0.5)
    ax.plot(dates, d_lows, color=DL_COLOR, alpha=0.5)
    ax.fill_between(dates, d_highs, d_lows, facecolor=DL_COLOR, alpha=0.1)

    ax.set_title("2021 Daily High and Low Temperatures - Sitka, AK & Death Valley, CA",
                 fontsize = 16)
    ax.set_xlabel("", fontsize=8)
    ax.set_ylabel("Temperature (F)", fontsize=12)
    ax.tick_params(labelsize=8)

    fig.autofmt_xdate()
    fig.canvas.manager.set_window_title("Sitka, AK v Death Valley, CA - Weather Comparison")

    plt.show()

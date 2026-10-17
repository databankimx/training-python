"""Assignment 16.09"""

# World Fires: In the resources for this chapter, you'll find a file called
#              world_fires_1_day.csv. This file contains information about fires
#              burning in different locations around the globe, including the
#              latitude and longitude, and the brightness of each fire.
#
#              Using the data processing work from the first part of this chapter
#              and the mapping work from this section, make a map that shows which
#              parts of the world are affected by fires. You can download more
#              recent versions of this data at:
#    https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data/.
#              You can find links to the data in CSV format in the TXT section.

from pathlib import Path
import csv
import plotly.express as px
from relative_paths import get_path

folder = "Data"
file_name = "MODIS_C6_1_USA_contiguous_and_Hawaii_24h.csv"
file_path = get_path(file_name, folder)

csv_file = Path(file_path)
lines = csv_file.read_text(encoding="UTF-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)

lat_index = header_row.index("latitude")
lon_index = header_row.index("longitude")
brt_index = header_row.index("brightness")

lats, lons, brts = [], [], []
for row in reader:
    try:
        lat = float(row[lat_index])
        lon = float(row[lon_index])
        brt = float(row[brt_index])
    except ValueError:
        print("Missing data!")
    else:
        lats.append(lat)
        lons.append(lon)
        brts.append(brt)

plot_title = "US Fires - Last 24 Hours"

fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=brts,
    title=plot_title,
    color=brts,
    color_continuous_scale="Hot",
    labels={"color": "Magnitude"},
    projection="albers usa"
)

fig.show()

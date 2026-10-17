"""Assignment 16.09"""
# World Fires: In the resources for this chapter, you'll find a file called
#              world_fires_1_day.csv. This file contains information about fires
#              burning in different locations around the globe, including the
#              latitude and longitude, and the brightness of each fire. Using
#              the data processing work from the first part of this chapter and
#              the mapping work from this section, make a map that shows which
#              parts of the world are affected by fires. You can download more
#              recent versions of this data at:
#   https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data/.
#              You can find links to the data in CSV format in the TXT section.

import os
import csv
import requests
from plotly.graph_objs import Layout
from plotly import offline

ROOT_DIR = os.path.dirname(__file__)

# pylint: disable=line-too-long
API_URL = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/noaa-20-viirs-c2/csv/J1_VIIRS_C2_Global_24h.csv"
LAT_LABEL = "latitude"
LON_LABEL = "longitude"
BRT_LABEL = "bright_ti4"

download = requests.get(API_URL, timeout=10)
content = download.content.decode("utf-8")

reader = csv.reader(content.splitlines(), delimiter=",")
header_row = next(reader)
lat_pos = header_row.index(LAT_LABEL)
lon_pos = header_row.index(LON_LABEL)
brt_pos = header_row.index(BRT_LABEL)

lats, lons, brts = [], [], []
for row in reader:
    lats.append(float(row[lat_pos]))
    lons.append(float(row[lon_pos]))
    brts.append(float(row[brt_pos]))

max_brt = max(brts)
data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "marker": {
        "size": [brt / max_brt * 10 for brt in brts],
        "color": [brt / max_brt for brt in brts],
        "colorscale": "Viridis",
        "reversescale": True,
        "colorbar": {"title": "Brightness"},
    },
}]

my_layout = Layout(title="Fires - Past 24 Hours")

fig = {"data": data, "layout": my_layout}
html_path = os.path.join(ROOT_DIR, "Data", "global_fires.html")

offline.plot(fig, filename=html_path)

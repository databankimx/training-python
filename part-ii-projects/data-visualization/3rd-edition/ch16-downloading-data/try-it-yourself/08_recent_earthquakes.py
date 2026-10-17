"""Assignment 16.08"""

# Recent Earthquakes: You can find data files containing information about the most
#                     recent earthquakes over 1-hour, 1-day, 7-day, and 30-day periods online.
#                     Go to https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
#                     and you'll see a list of links to data sets for various time periods,
#                     focusing on earthquakes of different magnitudes. Download one of these
#                     data sets, and create a visualization of the most recent earthquake
#                     activity.

import json
from pathlib import Path
import plotly.express as px
from relative_paths import get_path

folder = "Data"
filename = "readable_eq_data_30_day_serious_09102023.json"
filepath = get_path(filename, folder)

contents = Path(filepath).read_text(encoding="utf-8")
all_eq_data = json.loads(contents)
all_eq_dicts = all_eq_data["features"]

# Add a list for the earthquake titles
mags = [eq["properties"]["mag"] for eq in all_eq_dicts]
lons = [eq["geometry"]["coordinates"][0] for eq in all_eq_dicts]
lats = [eq["geometry"]["coordinates"][1] for eq in all_eq_dicts]
titles = [eq["properties"]["title"] for eq in all_eq_dicts]

# pylint: disable=consider-using-enumerate
for i in range(len(mags)):
    if mags[i] < 0:
        mags[i] *= -1

plot_title = all_eq_data["metadata"]["title"]

fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    title=plot_title,
    color=mags,
    color_continuous_scale="Viridis",
    labels={"color": "Magnitude"},
    projection="natural earth",
    hover_name=titles
)

fig.show()

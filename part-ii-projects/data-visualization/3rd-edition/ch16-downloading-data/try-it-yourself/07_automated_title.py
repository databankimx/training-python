"""Assignment 16.07"""

# Automated Title: In this section, we used the generic title Global Earthquakes.
#                  Instead, you can use the title for the dataset in the metadata
#                  part of the GeoJSON file. Pull this value and assign it to the
#                  variable `title`.

import json
from pathlib import Path
import plotly.express as px
from relative_paths import get_path

folder = "Data"
filename = "readable_eq_data_30_day_09102023.json"
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
    labels={"color":"Magnitude"},
    projection="natural earth",
    hover_name=titles
)

fig.show()

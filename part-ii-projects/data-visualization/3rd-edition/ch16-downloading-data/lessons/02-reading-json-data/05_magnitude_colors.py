"""Lesson 2.5: Magnitude Colors"""

import json
from pathlib import Path
from relative_paths import get_path
import plotly.express as px

folder = "Data"
# Include additional data (30 days)
filename = "readable_eq_data_30_day_09102023.json"
filepath = get_path(filename, folder)

contents = Path(filepath).read_text(encoding="utf-8")
all_eq_data = json.loads(contents)
all_eq_dicts = all_eq_data["features"]

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict["properties"]["mag"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])

# Some of the magnitudes came back as negative numbers in my download.
# So we'll clean those up
# pylint: disable=consider-using-enumerate
for i in range(len(mags)):
    if mags[i] < 0:
        mags[i] *= -1

plot_title = "Global Earthquakes"

# To see available color gradients/scales, do this:
# print(px.colors.named_colorscales())

fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    title=plot_title,
    # Set color gradient corresponding to magnitude
    color=mags,
    color_continuous_scale="Viridis",
    labels={"color":"Magnitude"},
    # Switch earth projection
    projection="natural earth"
)

fig.show()

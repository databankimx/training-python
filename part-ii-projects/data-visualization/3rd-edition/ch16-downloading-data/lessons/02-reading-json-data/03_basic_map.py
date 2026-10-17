"""Lesson 2.3: Basic Map"""

import json
from pathlib import Path
from relative_paths import get_path
# https://plotly.com/python/plotly-express
import plotly.express as px

folder = "Data"
filename = "readable_eq_data_1_day_09102023.json"
filepath = get_path(filename, folder)

contents = Path(filepath).read_text(encoding="UTF-8")
all_eq_data = json.loads(contents)
all_eq_dicts = all_eq_data["features"]

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict["properties"]["mag"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])

# Create the basic map plot
plot_title = "Global Earthquakes"
# The scatter_geo() function creates a scatter plot by lat/lon on a map of Earth
fig = px.scatter_geo(lat=lats, lon=lons, title=plot_title)

fig.show()

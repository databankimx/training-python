"""Assignment 16.07"""
# Automated Title: In this section, we specified the title manually when defining
#                  `my_layout`, which means we have to remember to update the title
#                  every time the source file changes. Instead, you can use the title
#                  for the data set in the metadata part of the JSON file. Pull this
#                  value, assign it to a variable, and use this for the title of the
#                  map when you're defining `my_layout`.

import json
from datetime import datetime
import os
from plotly.graph_objs import Layout
from plotly import offline

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Data", "eq_data_30_day_m1.json")

with open(file_path, encoding="UTF-8") as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]

mags = [eq_dict["properties"]["mag"] for eq_dict in all_eq_dicts]
lons = [eq_dict["geometry"]["coordinates"][0] for eq_dict in all_eq_dicts]
lats = [eq_dict["geometry"]["coordinates"][1] for eq_dict in all_eq_dicts]
hover_texts = [eq_dict["properties"]["title"] for eq_dict in all_eq_dicts]

data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "text": hover_texts,
    "marker": {
        "size": [3 * mag for mag in mags],
        "color": mags,
        "colorscale": "Viridis",
        "reversescale": True,
        "colorbar": {"title": "Magnitude"},
    },
}]

title_info = all_eq_data["metadata"]["title"].split(",")[0]
date_info = datetime.fromtimestamp(
    all_eq_dicts[0]["properties"]["time"] / 1000).strftime("[%b %Y]")
my_layout = Layout(title=f"{title_info} - {date_info}")

fig = {"data": data, "layout": my_layout}
html_path = os.path.join(ROOT_DIR, "Data", "global_earthquakes.html")

offline.plot(fig, filename=html_path)

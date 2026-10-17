"""Assignment 16.08"""
# Recent Earthquakes: You can find data files containing information about the most
#                     recent earthquakes over 1-hour, 1-day, 7-day, and 30-day periods
#                     online.
#                     Go to https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
#                     and you'll see a list of links to data sets for various time
#                     periods, focusing on earthquakes of different magnitudes. Download
#                     one of these data sets, and create a visualization of the most
#                     recent earthquake activity.

import os
import json
from plotly.graph_objs import Layout
from plotly import offline
import requests

API_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.geojson"
ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Data", "eq_data_last_30_days.json")

result = requests.get(API_URL, timeout=10).json()
with open(file_path, "w", encoding="UTF-8")as f:
    json.dump(result, f)

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

my_layout = Layout(title=all_eq_data["metadata"]["title"])

fig = {"data": data, "layout": my_layout}
html_path = os.path.join(ROOT_DIR, "Data", "global_earthquakes.html")

offline.plot(fig, filename=html_path)

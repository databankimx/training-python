"""Lesson 4 - Building a World Map (plotly)"""

import os
import json
# pylint: disable=unused-import
from plotly.graph_objs import Layout, Scattergeo
from plotly import offline

ROOT_DIR = os.path.dirname(__file__)

# file_path = os.path.join(ROOT_DIR, "Data", "eq_data_1_day_m1.json")
# file_path = os.path.join(ROOT_DIR, "Data", "eq_data_7_day_m1.json")
file_path = os.path.join(ROOT_DIR, "Data", "eq_data_30_day_m1.json")
with open(file_path, encoding = "UTF-8") as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]

url_template = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/IDTOKEN.geojson"
mags, lons, lats, hover_texts, urls = [], [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict["properties"]["mag"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])
    hover_texts.append(eq_dict["properties"]["title"])

    # I haven't figured out yet how to trigger a hyperlink from a scattergeo point,
    #   but I have code for storing them in case I figure that out
    net = {eq_dict["properties"]["net"]}
    code = {eq_dict["properties"]["code"]}
    id_token = f"{net}{code}".replace("{", "").replace("}", "").replace("'", "")
    urls.append(url_template.replace("IDTOKEN", id_token))

# Ex. 1
# data = [Scattergeo(lon = lons, lat = lats)]
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
    "customdata": urls
}]

my_layout = Layout(title = "Global Earthquakes")

fig = {"data": data, "layout": my_layout}
html_path = os.path.join(ROOT_DIR, "Data", "global_earthquakes.html")
offline.plot(fig, filename = html_path)

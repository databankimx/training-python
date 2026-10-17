"""Assignment 16.06"""
# Refactoring: The loop that pulls data from all_eq_dicts uses variables for the
#              magnitude, longitude, latitude, and title of each earthquake before
#              appending these values to their appropriate lists. This approach
#              was chosen for clarity in how to pull data from a JSON file, but
#              it's not necessary in your code. Instead of using these temporary
#              variables, pull each value from eq_dict and append it to the appropriate
#              list in one line. Doing so should shorten the body of this loop to
#              just four lines.

import json
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

my_layout = Layout(title="Global Earthquakes")
fig = {"data": data, "layout": my_layout}
html_path = os.path.join(ROOT_DIR, "Data", "global_earthquakes.html")

offline.plot(fig, filename=html_path)

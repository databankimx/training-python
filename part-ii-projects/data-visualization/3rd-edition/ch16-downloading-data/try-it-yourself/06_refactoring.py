"""Assignment 16.06"""

# Refactoring: The loop that pulls data from all_eq_dicts uses variables for the
#              magnitude, longitude, latitude, and title of each earthquake before
#              appending these values to their appropriate lists. This approach
#              was chosen for clarity in how to pull data from a JSON file, but
#              it's not necessary in your code. Instead of using these temporary
#              variables, pull each value from eq_dict and append it to the
#              appropriate list in one line. Doing so should shorten the body of
#              this loop to just four lines.

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

for i, mag in enumerate(mags):
    if mag < 0:
        mags[i] *= -1

plot_title = "Global Earthquakes"

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

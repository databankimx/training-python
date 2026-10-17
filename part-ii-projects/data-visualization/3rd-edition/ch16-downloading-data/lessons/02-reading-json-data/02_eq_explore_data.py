"""Lesson 2.2 - Exploring Earthquake JSON Data"""

# We are working with the GeoJSON format. It is useful to understand the organizationof its data
# Note: Fresh data can be retrieved here:
#       https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson

import json
from pathlib import Path
from relative_paths import get_path

folder = "Data"
filename = "readable_eq_data_1_day_09102023.json"
filepath = get_path(filename, folder)

# Explore the structure of the data
contents = Path(filepath).read_text(encoding="UTF-8")
all_eq_data = json.loads(contents)

# A good way to see if the JSON parses correctly is to:
# 1. Open the file in Notepad++
# 2. If you don't already have it, install the "JSTool" plugin
# 3. Click on Plugins > JSTool > JSON Viewer
# If the JSON parses correctly, it will appear as an explorable tree in a pop-out pane

# pylint: disable=line-too-long

#region JSON Structure:
#
# ROOT
# - type                = "Feature Collection"
#   - metadata          [Dictionary]
#     - generated       = <Timestamp>
#     - url             = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson"
#     - title           = "USGS Magnitude 1.0+ Earthquakes, Past Day"
#     - status          = <HTTP Response Code (expected = 200)>
#     - api             = <API Version>
#     - count           = <Item count in "features" array>
#   - features            [List]
#     - [i]               [Dictionary]
#       - type          = "Feature"
#       - properties      [Dictionary]
#         - mag         = <Magnitude>
#         - place       = <Descriptive Location>
#         - time        = <Timestamp - Occurrence>
#         - updated     = <Timestamp - Added to Data Source>
#         - tz          = <Time Zone>
#         - url         = <URL to Event Web Page: https://earthquake.usgs.gov/earthquakes/eventpage/{id}/executive>
#         - detail      = <URL to Detail API: https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/{id}.geojson
#         - felt
#         - cdi
#         - mmi
#         - alert
#         - status      = <Review Status>
#         - tsunami
#         - sig
#         - net         = <Station Network>
#         - code        = <Sequential Earthquake Num at Station>
#         - ids         = <Comma-delimited list of IDs>
#         - sources     = <Comma-delimited list of Stations>
#         - types       = <Comma-delimited list of recorded data types>
#         - nst
#         - dmin
#         - rms
#         - gap
#         - magType
#         - type        = <Feature Type: "earthquake">
#         - title       = <Descriptive Event Title>
#       - geometry        [Dictionary]
#         - type        = "Point"
#         - coordinates   [List]
#           - [0]       = <longitude>
#           - [1]       = <latitude>
#           - [2]       = <depth>
#         - id          = <Unique ID>
#       - id            = <Unique ID>
#     - [...]
#   - bbox          [List]
#     - [0]       = <min longitude>
#     - [1]       = <min latitude>
#     - [2]       = <min depth>
#     - [3]       = <max longitude>
#     - [4]       = <max latitude>
#     - [5]       = <max depth>
#endregion

# The "features" array contains objects describing each earthquake
all_eq_dicts = all_eq_data["features"]

# Count the number of earthquakes returned
suffix = "" if len(all_eq_dicts) == 1 else "s"
print(f"JSON file returned data for {len(all_eq_dicts)} earthquake{suffix}.")

# We are concerned with three data from each "features" object
# • Magnitude: item[properties][mag]
# • Longitude: item[geometry][coordinates][0]
# • Latitude:  item[geometry][coordinates][1]
# Note how GeoJSON lists longitude first to correspond to x,y coordinate systems

# Make lists of the important criteria
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict["properties"]["mag"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])

# Show that we parsed the data successfully
print(f"Last 10 magnitudes:\n{mags[-10:]}\n")
print(f"Last 5 longitudes:\n{lons[-5:]}\n")
print(f"Last 5 latitudes:\n{lats[-5:]}\n")

# We could use one list of dictionaries instead of three lists
data = []
for eq_dict in all_eq_dicts:
    quake_info = {
        "magnitude": eq_dict["properties"]["mag"],
        "longitude": eq_dict["geometry"]["coordinates"][0],
        "latitude": eq_dict["geometry"]["coordinates"][1]
    }
    data.append(quake_info)
print(f"Last Quake: {data[-1]}\n")
# But, as you'll see in the next lesson file, in this case, it's better to have separate lists

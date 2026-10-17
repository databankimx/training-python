"""Lesson 3.1 - Reading JSON Data"""

# Note: Fresh data can be retrieved here:
#       https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson

import json
import os

ROOT_DIR = os.path.dirname(__file__)

# Explore the structure of the data
file_path = os.path.join(ROOT_DIR, "Data", "eq_data_1_day_m1.json")
with open(file_path, encoding="UTF-8") as f:
    # Load the entire JSON file into memory
    all_eq_data = json.load(f)

# pylint: disable=line-too-long

# JSON Structure:
#region
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
#     - [0]               [Dictionary]
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

# Ex. 1
# formatted_file_path = os.path.join(ROOT_DIR, "Data", "readable_eq_data.json")
# with open(formatted_file_path, "w") as f:
#     # Store the JSON formatted to be readable (prettified)
#     json.dump(all_eq_data, f, indent = 4)

all_eq_dicts = all_eq_data["features"]

# Ex. 2
# suffix = "" if len(all_eq_dicts) == 1 else "s"
# print(f"JSON file returned data for {len(all_eq_dicts)} earthquake{suffix}.")

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict["properties"]["mag"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])
print(f"Last 10 magnitudes:\n{mags[:10]}")
print(f"Last 5 longitudes:\n{lons[:5]}")
print(f"Last 5 latitudes:\n{lats[:5]}")

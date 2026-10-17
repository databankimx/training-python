# Reading JSON Data

## Introduction

CSV files are good for tables, but much of the data on the web comes in JSON, the JavaScript Object
Notation format. JSON stores data as nested objects and lists, which can describe much more complicated
information than a flat table can.

This lesson reads a file of recent earthquakes from the United States Geological Survey (USGS). Each
earthquake is one entry in a list, and each entry holds a set of nested values. Before we can plot the
data, we need to find our way through its structure.

The `json` module is part of Python's standard library, so there is nothing extra to install. To get
fresh data, use the USGS feed linked in the script's comment.

---

## The Code

```python
"""Lesson 3.1 - Reading JSON Data"""

# Note: Fresh data can be retrieved here:
#       https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson

import json
import os

ROOT_DIR = os.path.dirname(__file__)

# Explore the structure of the data
file_path = os.path.join(ROOT_DIR, "data", "eq_data_1_day_m1.json")
with open(file_path, encoding="UTF-8") as f:
    # Load the entire JSON file into memory
    all_eq_data = json.load(f)

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
# formatted_file_path = os.path.join(ROOT_DIR, "data", "readable_eq_data.json")
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
```

---

### Walking Through the Code

**Loading the file.** `json.load()` reads the whole file and turns it into Python dictionaries and lists.
The result is a single dictionary, `all_eq_data`.

**Finding the structure.** The long comment describes the layout. The top level has a `features` list,
and each item in it is one earthquake. Inside each earthquake, `properties` holds the magnitude and
place, and `geometry` holds the coordinates.

**Reading values.** Each value is reached by following the keys down the structure. For example,
`eq_dict["properties"]["mag"]` is the magnitude of one earthquake.

**Collecting the data.** The loop goes through every earthquake, and adds its magnitude, longitude, and
latitude to three lists.

**Checking the result.** The three `print()` calls show a few values from each list. Printing a
little at a time is a good way to check that you're reading the right values before you plot them.

---

### Output

The terminal prints a few values from each list:

```
First 10 magnitudes:
[0.96, 1.2, 4.3, 3.6, 2.1, 4, 1.06, 2.3, 4.9, 1.8]
First 5 longitudes:
[-116.7941667, -148.9865, -74.2343, -161.6801, -118.5316667]
First 5 latitudes:
[33.4863333, 64.6673, -12.1025, 54.2232, 35.3098333]
```

---

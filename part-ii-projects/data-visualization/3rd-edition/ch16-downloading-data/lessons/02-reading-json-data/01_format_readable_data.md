# Formatting JSON Data

## Introduction

The earthquake data we downloaded is stored as JSON, and it came back as one long line of text. That's
correct for a computer, but it's hard for a person to read. This lesson reads the file, then writes it
back out with indentation, so the structure can be seen and explored.

Python's `json` module reads and writes JSON. It's part of the standard library, so there's nothing extra
to install.

---

## The Code

```python
"""Lesson 2.1 - Formatting JSON Data"""

import json
from pathlib import Path
from relative_paths import get_path

# Read in data from JSON file
folder = "data"
filename = "eq_data_1_day_09102023.json"
filepath = get_path(filename, folder)

contents = Path(filepath).read_text(encoding="utf-8")
all_eq_data = json.loads(contents)

# Reformat the JSON data and store as a new file
formatted_filename = "readable_" + filename
formatted_filepath = get_path(formatted_filename, folder)

path = Path(formatted_filepath)
# The indent argument sets how many spaces are added for each level of indentation
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents, encoding="UTF-8")
```

---

### Walking Through the Code

**Reading the data.** `json.loads()` turns the text of the file into Python dictionaries and lists.

**Writing it back.** `json.dumps()` turns the data back into text. `indent=4` puts four spaces at each
level of nesting, so every key sits on its own line.

**A new file.** The formatted text is saved as `readable_eq_data_1_day_09102023.json`, beside the original.
The original file is left unchanged.

---

### Output

This script prints nothing. It writes a new file, `data/readable_eq_data_1_day_09102023.json`. The full
file has 149 earthquakes and runs to thousands of lines, so only the start is shown here:

```json
{
    "type": "FeatureCollection",
    "metadata": {
        "generated": 1694346994000,
        "url": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson",
        "title": "USGS Magnitude 1.0+ Earthquakes, Past Day",
        "status": 200,
        "api": "1.10.3",
        "count": 149
    },
    "features": [
        {
            "type": "Feature",
            "properties": {
                "mag": 4.2,
                "place": "41 km SSW of Ollag\u00fce, Chile",
                "time": 1694344093177,
                "updated": 1694346139040,
                "tz": null,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000kusz",
                "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000kusz.geojson",
                "felt": null,
                "cdi": null,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 271,
                "net": "us",
                "code": "7000kusz",
                "ids": ",us7000kusz,",
                "sources": ",us,",
                "types": ",origin,phase-data,",
                "nst": 15,
                "dmin": 1.119,
                "rms": 0.24,
                "gap": 106,
                "magType": "mb",
                "type": "earthquake",
                "title": "M 4.2 - 41 km SSW of Ollag\u00fce, Chile"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -68.426,
                    -21.5675,
                    131.917
                ]
            },
            "id": "us7000kusz"
        },
        ...
    ],
    "bbox": [
        ...
    ]
}
```

Each earthquake is one item in the `features` list, and each item has the same nested layout as the
first one. Open the file in a text editor to explore the rest.

---

# Another API: Hacker News Article

## Introduction

The GitHub API in the last chapter returned a list of repositories. This lesson uses a different API, from
Hacker News, a site where people share and discuss technology articles. Each item on Hacker News, whether a
story, a comment, or a poll, has its own address in the API. This lesson fetches one story and saves the
response so you can explore its structure.

Hacker News is run by Y Combinator, and its API is public. The `requests` library makes the call, and the
`json` module saves the file.

---

## The Code

```python
"""Lesson 3.1 - Another API: Hacker News"""

import json
import os
import requests

ROOT_DIR = os.path.dirname(__file__)

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url, timeout=10)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()
readable_file = os.path.join(ROOT_DIR, "data", "readable_hn_data.json")
with open(readable_file, "w", encoding="UTF-8") as f:
    json.dump(response_dict, f, indent = 4)
```

---

### Walking Through the Code

**The item address.** Hacker News gives each item a number, and the address ends with that number. The
address here, `item/19155826.json`, is one story.

**Checking the request.** The status code is printed, as in the earlier lessons.

**Saving the response.** `r.json()` turns the response into a dictionary. `json.dump()` writes it to
`data/readable_hn_data.json` with four spaces of indentation, so the structure is easy to read in a text
editor.

**Exploring the file.** The next lesson uses the same API to list the top stories, and it shows how the
fields of each story are used. Open the saved file to see the fields for this one.

---

### Output

The terminal prints the status code, which should be 200 for a successful request. The script also saves
`data/readable_hn_data.json`, which you can open in a text editor.

```
Status code: 200
```

The saved file holds the whole story, indented as the script wrote it:

```json
{
    "by": "jimktrains2",
    "descendants": 221,
    "id": 19155826,
    "kids": [
        19156572,
        19158857,
        19156773,
        19157251,
        19156415,
        19159820,
        19157154,
        19156385,
        19156489,
        19158522,
        19156755,
        19156974,
        19158319,
        19157034,
        19156935,
        19158935,
        19157531,
        19158638,
        19156466,
        19156758,
        19156565,
        19156498,
        19156335,
        19156041,
        19156704,
        19159047,
        19159127,
        19156217,
        19156375,
        19157945
    ],
    "score": 728,
    "time": 1550085414,
    "title": "Nasa\u2019s Mars Rover Opportunity Concludes a 15-Year Mission",
    "type": "story",
    "url": "https://www.nytimes.com/2019/02/13/science/mars-opportunity-rover-dead.html"
}
```

---

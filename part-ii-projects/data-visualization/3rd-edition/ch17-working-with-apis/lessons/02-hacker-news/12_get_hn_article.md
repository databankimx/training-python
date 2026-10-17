# Getting a Single Article

## Introduction

The GitHub lessons used a search that returns a list. The Hacker News API works differently: each item, such as a
story, comment, or poll, has its own address, and you fetch it by its number. This lesson fetches one story and
prints its full structure, so you can see the fields it has.

---

## The Code

```python
"""Lesson 2.12 - Getting a Single Article"""

import json
import sys
import requests

# Reference:    https://github.com/HackerNews/API
# Make an API call for a single article, and store the response
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"

response = requests.get(url, timeout=10)
print(f"Response Status: {response.status_code}")

# Explore the structure of the data
response_dict = response.json()

# Check to see if the request succeeded
if response.status_code != 200:
    print(f"API connection to [{url}] failed\n\twith status code: {response.status_code}")
    sys.exit(-1)

# If that worked, we can access the resulting JSON from the response.
print("Success:")
response_string = json.dumps(response_dict, indent=4)
print(response_string)
```

---

### Walking Through the Code

**The item address.** Hacker News items are numbered. The address ends with the item's number, so changing the number
fetches a different story.

**Printing the structure.** `json.dumps(..., indent=4)` prints the whole response with indentation, so each field and
any nested lists are easy to see.

---

### Output

The terminal prints the response status, then the story as indented JSON:

```
[sample output to be added]
```

---

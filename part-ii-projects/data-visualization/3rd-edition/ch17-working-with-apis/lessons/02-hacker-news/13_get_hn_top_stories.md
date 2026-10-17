# Getting a List of Top Articles

## Introduction

The last lesson fetched one story. This lesson gets the list of current top stories, then makes a separate request for
each of the first five. It collects the title, link, and number of comments for each, and prints them sorted by
comments, so the most discussed stories come first.

---

## The Code

```python
"""Lesson 2.13 - Getting a List of Top Articles"""

import sys
from operator import itemgetter
import requests

# Make an API call for a list of top articles, and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"

response = requests.get(url, timeout=10)
print(f"Response Status: {response.status_code}")

if response.status_code != 200:
    print(f"API connection to [{url}] failed\n\twith status code: {response.status_code}")
    sys.exit(-1)

submission_ids = response.json()
submission_dicts = []
# Get more info on first five submissions
for submission_id in submission_ids[:5]:
    # Call the API to get the specific article
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    response = requests.get(url, timeout=10)
    print(f"{submission_id} Status: {response.status_code}")
    response_dict = response.json()

    # Build a dictionary for each article
    submission_dict = {
        "title": response_dict["title"],
        "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
        "comments": response_dict["descendants"] if "descendants" in response_dict.keys() else 0
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion Link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
```

---

### Walking Through the Code

**The list of IDs.** The `topstories` address returns a list of item numbers. `submission_ids[:5]` keeps the first five.

**One request per story.** The loop builds each story's address from its number and fetches it. The status of each
request is printed as it goes.

**Sorting.** `sorted()` with `itemgetter("comments")` orders the stories by their comment counts, and `reverse=True`
puts the largest first.

**Missing comment counts.** Some stories have no `descendants` field, which means they have no comments yet. The
code checks for the field and uses zero when it's missing, so those stories are still listed, at the bottom of the sorted
list.

---

### Output

The terminal prints the status of each request, then the five stories, most discussed first:

```
Response Status: 200
50129121 Status: 200
50106747 Status: 200
50112657 Status: 200
50131256 Status: 200
50127979 Status: 200

Title: Tesla Roadster
Discussion Link: https://news.ycombinator.com/item?id=50112657
Comments: 2747

Title: DeepSeek: DeepSeek v4.1 Flash 1017
Discussion Link: https://news.ycombinator.com/item?id=50129121
Comments: 168

Title: Ultramarine 1 Flash
Discussion Link: https://news.ycombinator.com/item?id=50106747
Comments: 100

Title: Show HN: Llmspeed – feel how fast a local LLM runs before you buy the hardware
Discussion Link: https://news.ycombinator.com/item?id=50127979
Comments: 51

Title: Solar surpasses nuclear power globally for first time – pv magazine Global
Discussion Link: https://news.ycombinator.com/item?id=50131256
Comments: 2
```

---

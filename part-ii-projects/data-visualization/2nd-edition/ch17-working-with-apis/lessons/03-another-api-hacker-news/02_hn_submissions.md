# Another API: Hacker News Submissions

## Introduction

The last lesson fetched a single Hacker News story. This lesson gets the list of current top stories, then
makes a separate API call for each of the first ten. It builds a small dictionary for each story, then sorts
the stories by how many comments they have, so the most discussed stories come first.

---

## The Code

```python
"""Lesson 3.2 - Another API: Hacker News"""

from operator import itemgetter
import requests

# Make an API call and store the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url, timeout=10)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url, timeout=10)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        "title": response_dict["title"],
        "hn_link": f"http://news.ycombinator.com/item?id={submission_id}",
        # Book code fails when there is an item with no comments,
        #     so default to zero if "descendants" is missing
        "comments": response_dict["descendants"] if "descendants" in response_dict.keys() else 0,
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
```

---

### Walking Through the Code

**The list of IDs.** The `topstories` address returns a list of item numbers, one for each current top story.
`submission_ids[:10]` takes the first ten.

**One call per story.** The loop builds each story's address from its ID and makes a separate request. It
prints the ID and the status of each request as it goes, so you can see any that fail.

**Building the dictionary.** Each story becomes a dictionary with its title, a link to its discussion page,
and its number of comments. Some stories have no `descendants` field, which is the comment count, so the
code uses zero for those.

**Sorting.** `sorted()` with `itemgetter("comments")` orders the stories by comment count, and `reverse=True`
puts the largest counts first.

---

### Output

The terminal prints the status of each request, then the ten stories, most discussed first. Each story shows
its title, its discussion link, and its number of comments. The stories change as the site changes, so your
output will differ from this example.

```
Status code: 200
id: 50129121    status: 200
id: 50106747    status: 200
id: 50112657    status: 200
id: 50127979    status: 200
id: 50129045    status: 200
id: 50122431    status: 200
id: 50122878    status: 200
id: 50104783    status: 200
id: 50103255    status: 200
id: 50122800    status: 200

Title: Tesla Roadster
Discussion link: http://news.ycombinator.com/item?id=50112657
Comments: 2697

Title: Claude reveals ECDSA curve origins
Discussion link: http://news.ycombinator.com/item?id=50122800
Comments: 339

Title: DeepSeek: DeepSeek v4.1 Flash 1017
Discussion link: http://news.ycombinator.com/item?id=50129121
Comments: 130

Title: DeepSeek-v4.1-Flash-1017
Discussion link: http://news.ycombinator.com/item?id=50129045
Comments: 101

Title: Ultramarine 1 Flash
Discussion link: http://news.ycombinator.com/item?id=50106747
Comments: 92

Title: You could have invented transformers from memory
Discussion link: http://news.ycombinator.com/item?id=50122878
Comments: 80

Title: Llama.cpp on a jailbroken PS5: run any GGUF model natively on the console
Discussion link: http://news.ycombinator.com/item?id=50122431
Comments: 76

Title: Show HN: Llmspeed – feel how fast a local LLM runs before you buy the hardware
Discussion link: http://news.ycombinator.com/item?id=50127979
Comments: 47

Title: Intuitive concurrent programming in any language
Discussion link: http://news.ycombinator.com/item?id=50103255
Comments: 16

Title: Recipes Are Moving from Maven Central to the Code Genome Project
Discussion link: http://news.ycombinator.com/item?id=50104783
Comments: 5
```

---

# Working with Results

## Introduction

The last lesson made the request and read the total. This lesson works with the rest of the response: it
counts the repositories returned, checks that the results are complete, and examines the structure of the
first repository, so we know which fields are available.

---

## The Code

```python
"""Lesson 1.2 - Working with Results"""

import sys
import requests

url = "https://api.github.com/search/repositories"
query_string = "?q=language:python+sort:stars+stars:>10000"
request_url = url + query_string
headers = {"Accept": "application/vnd.github.v3+json"}

response = requests.get(request_url, headers=headers, timeout=10)
print(f"Status code: {response.status_code}")

response_dict = response.json()

if response.status_code != 200:
    print(f"API connection to [{url}] failed\n\twith status code: {response.status_code}")
    sys.exit(-1)

print("Success:")

# Count the number of repositories returned
print(f"- Total repositories: {response_dict['total_count']}")
print(f"- Complete results: {not response_dict['incomplete_results']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the structure of the first repository.
repo_dict = repo_dicts[0]
print(f"- Keys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print("  -", key)
```

---

### Walking Through the Code

**Counting results.** `total_count` is the number of repositories that match the search. `items` holds the
repositories GitHub returned for this page of results, which is at most 30.

**Complete results.** `incomplete_results` is `True` when GitHub could not finish the search in time. The
script prints the opposite, so `True` means the results are complete.

**The structure of one repository.** `repo_dicts[0]` is the first repository. Printing its sorted keys shows
every field GitHub provides for a repository, so you know what is available to use in the next lessons.

---

### Output

The terminal prints the counts, then the number of keys in the first repository and each key name:

```
[sample output to be added]
```

---

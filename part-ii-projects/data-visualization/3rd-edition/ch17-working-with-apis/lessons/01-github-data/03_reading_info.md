# Reading Information

## Introduction

The last lesson listed the fields of one repository. This lesson picks out the most useful of them, such as the
name, owner, stars, link, dates, and description, and prints them for the first repository in the results.

---

## The Code

```python
"""Lesson 1.3 - Reading Information"""

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

print(f"- Total repositories: {response_dict['total_count']}")
print(f"- Complete results: {not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

repo_dict = repo_dicts[0]
print("\nSelected information about first repository:")
# Review some of the key info about the first repository
print(f"- Name: {repo_dict['name']}")
print(f"- Owner: {repo_dict['owner']['login']}")
print(f"- Stars: {repo_dict['stargazers_count']}")
print(f"- Repository: {repo_dict['html_url']}")
print(f"- Created: {repo_dict['created_at']}")
print(f"- Updated: {repo_dict['updated_at']}")
print(f"- Description: {repo_dict['description']}")
```

---

### Walking Through the Code

**Nested values.** The owner's name is inside the `owner` dictionary, so it's reached with
`repo_dict['owner']['login']`. Each level of nesting adds another pair of square brackets.

**Choosing fields.** Each line picks one field from the dictionary and labels it. The fields are the same ones we
listed in the last lesson.

---

### Output

The terminal prints the summary, then the key details of the first repository:

```
Status code: 200
Success:
- Total repositories: 1038
- Complete results: True
Repositories returned: 30

Selected information about first repository:
- Name: public-apis
- Owner: public-apis
- Stars: 489641
- Repository: https://github.com/public-apis/public-apis
- Created: 2016-03-20T23:49:42Z
- Updated: 2026-10-17T13:51:09Z
- Description: A collective list of free APIs
```

---

# Summarizing Top Repositories

## Introduction

The last lesson printed the details of one repository. This lesson loops over every repository in the results
and prints a summary of each, so you can compare the top Python projects side by side.

---

## The Code

```python
"""Lesson 1.4 - Summarizing Top Repositories"""

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

print("\nSelected information about each repository:")

for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"- Owner: {repo_dict['owner']['login']}")
    print(f"- Stars: {repo_dict['stargazers_count']}")
    print(f"- Repository: {repo_dict['html_url']}")
    print(f"- Description: {repo_dict['description']}\n")
```

---

### Walking Through the Code

**Looping over the results.** The `for` loop runs once for each repository in `repo_dicts`, so the same four
lines of output are printed for every repository.

**Blank lines.** The `\n` at the end of the description line adds a blank line after each repository, which keeps
the list easy to scan.

---

### Output

The terminal prints the summary, then the name, owner, stars, link, and description of each repository:

```
Status code: 200
Success:
- Total repositories: 1038
- Complete results: True
Repositories returned: 30

Selected information about each repository:
Name: public-apis
- Owner: public-apis
- Stars: 489641
- Repository: https://github.com/public-apis/public-apis
- Description: A collective list of free APIs

Name: free-programming-books
- Owner: EbookFoundation
- Stars: 399307
- Repository: https://github.com/EbookFoundation/free-programming-books
- Description: :books: Freely available programming books

...

Name: DeepSeek-V3
- Owner: deepseek-ai
- Stars: 104504
- Repository: https://github.com/deepseek-ai/DeepSeek-V3
- Description: None
```

---

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
Status code: 200
Success:
- Total repositories: 1038
- Complete results: True
Repositories returned: 30
- Keys: 82
  - allow_forking
  - archive_url
  - archived
  - assignees_url
  - blobs_url
  - branches_url
  - clone_url
  - collaborators_url
  - comments_url
  - commits_url
  - compare_url
  - contents_url
  - contributors_url
  - created_at
  - default_branch
  - deployments_url
  - description
  - disabled
  - downloads_url
  - events_url
  - fork
  - forks
  - forks_count
  - forks_url
  - full_name
  - git_commits_url
  - git_refs_url
  - git_tags_url
  - git_url
  - has_discussions
  - has_downloads
  - has_issues
  - has_pages
  - has_projects
  - has_pull_requests
  - has_wiki
  - homepage
  - hooks_url
  - html_url
  - id
  - is_template
  - issue_comment_url
  - issue_events_url
  - issues_url
  - keys_url
  - labels_url
  - language
  - languages_url
  - license
  - merges_url
  - milestones_url
  - mirror_url
  - name
  - node_id
  - notifications_url
  - open_issues
  - open_issues_count
  - owner
  - private
  - pull_request_creation_policy
  - pulls_url
  - pushed_at
  - releases_url
  - score
  - size
  - ssh_url
  - stargazers_count
  - stargazers_url
  - statuses_url
  - subscribers_url
  - subscription_url
  - svn_url
  - tags_url
  - teams_url
  - topics
  - trees_url
  - updated_at
  - url
  - visibility
  - watchers
  - watchers_count
  - web_commit_signoff_required
```

---

# Processing an API Response

## Introduction

So far the data in this course has come from files. Much of the data on the web is available through an
**API**, an application programming interface. You send a request to a web address, and the service sends
back the data, usually as JSON.

This lesson calls the GitHub API to ask for the most-starred Python projects. It reads the response, which
is a dictionary, and prints some of the details about each project. The `requests` library makes the call.

Set up a GitHub token before you start, so the exercises aren't held back by GitHub's rate limit. The steps are in `github-token-setup.md`, in the `data-visualization` folder.

Install `requests` before running this lesson:

```bash
python -m pip install requests
```

---

## The Code

```python
"""Lesson 1 - Processing an API Response"""

# Note: You'll probably need to install the requests plug-in
# > python -m pip install requests

import requests

# Make an API call and store the response.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers, timeout=10)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()

# Ex 1
# print(response_dict.keys())
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")

# Ex 2
# repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()): print(key)

# Ex 3
# print(f"Name: {repo_dict['name']}")
# print(f"Owner: {repo_dict['owner']['login']}")
# print(f"Stars: {repo_dict['stargazers_count']}")
# print(f"Repository: {repo_dict['html_url']}")
# print(f"Created: {repo_dict['created_at']}")
# print(f"Updated: {repo_dict['updated_at']}")
# print(f"Description: {repo_dict['description']}")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
    input("Press <ENTER> to continue...")
```

---

### Walking Through the Code

**Making the request.** `requests.get()` sends the request to the GitHub address. The `url` includes a
search for Python repositories, sorted by stars. `timeout=10` stops the script waiting forever if the
service doesn't reply.

**Checking the response.** `r.status_code` is the HTTP status. A value of 200 means the request succeeded.

**Reading the dictionary.** `r.json()` turns the response into a Python dictionary. The `items` key holds
a list, with one dictionary for each repository.

**Printing details.** The loop prints the name, owner, stars, link, dates, and description of each
repository. `input()` waits for Enter before showing the next one, so you can read each entry in turn.

**The exercises.** The `# Ex 1`, `# Ex 2`, and `# Ex 3` blocks are the exercises from the textbook. To run one,
remove the `#` from the start of its lines and leave the rest of the file as it is. Exercise 1 needs only the
`print(response_dict.keys())` line, which lists the top-level keys of the response. Exercise 2 needs the whole
block beginning `repo_dict = repo_dicts[0]`. Exercise 3 uses `repo_dict`, so uncomment the `repo_dict` line in
Exercise 2 along with the Exercise 3 block. The loop at the end of the file still runs after the exercises, so
the full list of repositories is printed too.

---

### Output

The terminal prints the status code and the total number of repositories GitHub holds for this search. It
then shows each repository in turn, waiting for Enter after each one. The total and the list change over
time, so your output will differ from this example.

```
Status code: 200
Total repositories: 34900333
Repositories returned: 30

Selected information about each repository:

Name: public-apis
Owner: public-apis
Stars: 489635
Repository: https://github.com/public-apis/public-apis
Created: 2016-03-20T23:49:42Z
Updated: 2026-10-17T13:11:19Z
Description: A collective list of free APIs
Press <ENTER> to continue...

Name: free-programming-books
Owner: EbookFoundation
Stars: 399299
Repository: https://github.com/EbookFoundation/free-programming-books
Created: 2013-10-11T06:50:37Z
Updated: 2026-10-17T13:09:02Z
Description: :books: Freely available programming books
Press <ENTER> to continue...

...

Name: DeepSeek-V3
Owner: deepseek-ai
Stars: 104502
Repository: https://github.com/deepseek-ai/DeepSeek-V3
Created: 2024-12-26T09:52:40Z
Updated: 2026-10-17T11:57:15Z
Description: None
Press <ENTER> to continue...
```

#### Exercise 2: The Keys of One Repository

Uncomment the `# Ex 2` block to print the number of keys in one repository's dictionary, followed by each key in
alphabetical order. Each repository has the same keys, so this shows every field GitHub provides:

```

Keys: 82
allow_forking
archive_url
archived
assignees_url
blobs_url
branches_url
clone_url
collaborators_url
comments_url
commits_url
compare_url
contents_url
contributors_url
created_at
default_branch
deployments_url
description
disabled
downloads_url
events_url
fork
forks
forks_count
forks_url
full_name
git_commits_url
git_refs_url
git_tags_url
git_url
has_discussions
has_downloads
has_issues
has_pages
has_projects
has_pull_requests
has_wiki
homepage
hooks_url
html_url
id
is_template
issue_comment_url
issue_events_url
issues_url
keys_url
labels_url
language
languages_url
license
merges_url
milestones_url
mirror_url
name
node_id
notifications_url
open_issues
open_issues_count
owner
private
pull_request_creation_policy
pulls_url
pushed_at
releases_url
score
size
ssh_url
stargazers_count
stargazers_url
statuses_url
subscribers_url
subscription_url
svn_url
tags_url
teams_url
topics
trees_url
updated_at
url
visibility
watchers
watchers_count
web_commit_signoff_required
```

The key list is long, but it's worth scanning. Many of the keys are web addresses for other parts of the
API, such as `commits_url` and `issues_url`, and each one can be followed to fetch more data.

#### Exercise 3: The Details of One Repository

Uncomment the `repo_dict = repo_dicts[0]` line in Exercise 2, then the Exercise 3 block. The script prints the
name, owner, stars, link, dates, and description of the first repository, before the full list. The output
below shows the start of the run, and the full list of repositories follows it:

```
Status code: 200
Total repositories: 34899918
Repositories returned: 30
Name: public-apis
Owner: public-apis
Stars: 489637
Repository: https://github.com/public-apis/public-apis
Created: 2016-03-20T23:49:42Z
Updated: 2026-10-17T13:17:52Z
Description: A collective list of free APIs
```

---

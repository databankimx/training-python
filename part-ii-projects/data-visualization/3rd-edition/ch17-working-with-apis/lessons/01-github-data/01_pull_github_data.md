# GitHub Data

## Introduction

This lesson starts a series that uses the GitHub API to explore the Python projects on GitHub. The series
shows how to make an API request, check that it worked, and read the response, in a form that is easy to
build on in the later lessons.

The `requests` library makes the call. Install it first if you haven't already:

```bash
python -m pip install requests
```

---

## The Code

```python
"""Lesson 1.1 - GitHub Data"""

import sys
# We use the requests library to perform API calls over the internet.
import requests
# > python -m pip install requests

# We are going to connect to the API exposed by GitHub
# Reference:    https://docs.github.com/en/rest
url = "https://api.github.com/search/repositories"
# We will search for repositories using python with greater than 10K stars,
#     sorted by number of stars.
query_string = "?q=language:python+sort:stars+stars:>10000"
# Combine the base URL and query string to get the full request URL
request_url = url + query_string

# We use a dictionary to define the headers we will include in the request.
#     Not all APIs require the same headers.
headers = {"Accept": "application/vnd.github.v3+json"}

# We'll make a request to our URL with the specified headers
response = requests.get(request_url, headers=headers, timeout=10)

# Assuming we were successful, the HTTP response code should be 200
print(f"Status code: {response.status_code}")

response_dict = response.json()

# Check to see if the request succeeded

if response.status_code != 200:
    print(f"API connection to [{url}] failed\n\twith status code: {response.status_code}")
    sys.exit(-1)
elif "message" in response_dict:
    # Otherwise, there may be "message" and "errors" keys in the response dictionary
    print("Error:", response_dict["message"])
else:
    print(f"Success:\n - Total repositories: {response_dict['total_count']}")
```

---

### Walking Through the Code

**The address.** `url` is the base address of GitHub's repository search. `query_string` holds the search itself:
Python repositories, with more than 10,000 stars, sorted by the number of stars. Joining the two gives the full
request address.

**The headers.** The `Accept` header tells GitHub which version of its API format to use. Not every API needs
headers, but this one does.

**Checking the response.** The status code is printed first. The script then checks the code and, if the
response contains a `message` key, prints it as an error. Only when both checks pass does it print the total
number of repositories.

---

### Output

The terminal prints the status code, then the result of the checks:

```
[sample output to be added]
```

---

# Checking API Limits

## Introduction

GitHub limits how many requests you can make in a period of time. If you exceed that limit, the API stops
answering with data. This lesson asks GitHub for the current state of your limits, so you can see how many
requests remain.

---

## The Code

```python
"""Lesson 1.5 - Checking API Limits"""

import json
import requests

# We can use this to see if we're running afoul of the API limits on GitHub

url = "https://api.github.com/rate_limit"
headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers, timeout=10)
print(json.dumps(response.json(), indent=4))
```

---

### Walking Through the Code

**A separate address.** The `rate_limit` address reports on your limits. It doesn't count against them in the
same way as a search, so it's safe to check often.

**Readable output.** `json.dumps(..., indent=4)` prints the response with indentation, so each limit and its
reset time is easy to read.

---

### Output

The terminal prints the rate limit details as indented JSON. The numbers change as you make requests, so your
output will differ from this example.

```json
{
    "resources": {
        "code_search": {
            "limit": 60,
            "remaining": 60,
            "reset": 1792249120,
            "used": 0
        },
        "core": {
            "limit": 60,
            "remaining": 60,
            "reset": 1792249120,
            "used": 0
        },
        "graphql": {
            "limit": 0,
            "remaining": 0,
            "reset": 1792249120,
            "used": 0
        },
        "integration_manifest": {
            "limit": 5000,
            "remaining": 5000,
            "reset": 1792249120,
            "used": 0
        },
        "search": {
            "limit": 10,
            "remaining": 10,
            "reset": 1792245580,
            "used": 0
        }
    },
    "rate": {
        "limit": 60,
        "remaining": 60,
        "reset": 1792249120,
        "used": 0
    }
}
```

---

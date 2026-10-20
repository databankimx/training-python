"""Lesson 1.5 - Checking API Limits"""

import os  # for the GITHUB_TRAINING_TOKEN environment variable
import json
import requests

# We can use this to see if we're running afoul of the API limits on GitHub

url = "https://api.github.com/rate_limit"
headers = {"Accept": "application/vnd.github.v3+json"}
# An authenticated request gets a higher limit. See github-token-setup.md.
if os.environ.get("GITHUB_TRAINING_TOKEN"):
    headers["Authorization"] = f"Bearer {os.environ['GITHUB_TRAINING_TOKEN']}"
response = requests.get(url, headers=headers, timeout=10)
print(json.dumps(response.json(), indent=4))

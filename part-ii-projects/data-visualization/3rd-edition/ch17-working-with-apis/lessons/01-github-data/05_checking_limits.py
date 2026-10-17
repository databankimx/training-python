"""Lesson 1.5 - Checking API Limits"""

import json
import requests

# We can use this to see if we're running afoul of the API limits on GitHub

url = "https://api.github.com/rate_limit"
headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers, timeout=10)
print(json.dumps(response.json(), indent=4))

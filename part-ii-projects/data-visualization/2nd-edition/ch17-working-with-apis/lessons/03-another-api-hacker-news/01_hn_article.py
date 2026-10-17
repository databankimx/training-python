"""Lesson 3.1 - Another API: Hacker News"""

import json
import os
import requests

ROOT_DIR = os.path.dirname(__file__)

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url, timeout=10)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()
readable_file = os.path.join(ROOT_DIR, "Data", "readable_hn_data.json")
with open(readable_file, "w", encoding="UTF-8") as f:
    json.dump(response_dict, f, indent = 4)

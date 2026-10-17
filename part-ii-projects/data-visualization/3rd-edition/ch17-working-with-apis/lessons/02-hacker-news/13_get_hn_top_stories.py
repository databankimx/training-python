"""Lesson 2.13 - Getting a List of Top Articles"""

import sys
from operator import itemgetter
import requests

# Make an API call for a list of top articles, and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"

response = requests.get(url, timeout=10)
print(f"Response Status: {response.status_code}")

if response.status_code != 200:
    print(f"API connection to [{url}] failed\n\twith status code: {response.status_code}")
    sys.exit(-1)

submission_ids = response.json()
submission_dicts = []
# Get more info on first five submissions
for submission_id in submission_ids[:5]:
    # Call the API to get the specific article
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    response = requests.get(url, timeout=10)
    print(f"{submission_id} Status: {response.status_code}")
    response_dict = response.json()

    # Build a dictionary for each article
    submission_dict = {
        "title": response_dict["title"],
        "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
        "comments": response_dict["descendants"]
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion Link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

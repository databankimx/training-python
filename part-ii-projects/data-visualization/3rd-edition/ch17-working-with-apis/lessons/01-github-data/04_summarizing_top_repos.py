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

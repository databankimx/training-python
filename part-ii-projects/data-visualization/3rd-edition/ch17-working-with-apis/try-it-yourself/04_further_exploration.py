"""Assignment 17.04"""

# Further Exploration: Visit the documentation for Plotly and either the GitHub
#                      API or the Hacker News API. Use some of the information
#                      you find there to either customize the style of the plots
#                      we've already made or pull some different information and
#                      create your own visualizations.

import os  # for the GITHUB_TRAINING_TOKEN environment variable
import sys
import requests
import plotly.express as px

# Pull the same GitHub data as before, but chart two numbers against each other
url = "https://api.github.com/search/repositories"
query_string = "?q=language:python+sort:stars+stars:>10000"
request_url = url + query_string
headers = {"Accept": "application/vnd.github.v3+json"}
# An authenticated request gets a higher limit. See github-token-setup.md.
if os.environ.get("GITHUB_TRAINING_TOKEN"):
    headers["Authorization"] = f"Bearer {os.environ['GITHUB_TRAINING_TOKEN']}"
response = requests.get(request_url, headers=headers, timeout=10)

if response.status_code != 200:
    print(f"API connection to [{url}] failed\n\twith status code: {response.status_code}")
    sys.exit(-1)

repo_dicts = response.json()["items"]
names = [repo["name"] for repo in repo_dicts]
stars = [repo["stargazers_count"] for repo in repo_dicts]
forks = [repo["forks_count"] for repo in repo_dicts]

# The dark template restyles the whole chart, and the colors show the star count
title = "Python Repositories: Stars against Forks"
labels = {"x": "Forks", "y": "Stars"}
fig = px.scatter(
    x=forks, y=stars, title=title, labels=labels, hover_name=names,
    color=stars, color_continuous_scale="Viridis", template="plotly_dark"
)
fig.update_traces(marker_size=14)
fig.update_layout(title_font_size=24, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update(layout_coloraxis_showscale=True)

fig.show()

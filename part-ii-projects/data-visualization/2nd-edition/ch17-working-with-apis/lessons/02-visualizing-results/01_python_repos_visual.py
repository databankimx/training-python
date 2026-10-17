"""Lesson 2.1 - Visualizing Results"""

import os
import sys
import requests
from plotly import offline

ROOT_DIR = os.path.dirname(__file__)

# Make an API call and store the response.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
# An authenticated request gets a higher limit. See github-token-setup.md.
if os.environ.get("GITHUB_TRAINING_TOKEN"):
    headers["Authorization"] = f"Bearer {os.environ['GITHUB_TRAINING_TOKEN']}"

r = requests.get(url, headers=headers, timeout=10)
if r.status_code != 200:
    print(f"Failed to consume API!\n Status: {r.status_code}")
    sys.exit(-1)

response_dict = r.json()
repo_dicts = response_dict["items"]

repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict["stargazers_count"])

    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    label = f"{owner}<br />{description}"
    labels.append(label)

# Make visualization.
data = [{
    "type": "bar",
    "x": repo_links,
    "y": stars,
    "hovertext": labels,
    "marker": {
        "color": "rgb(60, 100, 150)",
        "line": {"width": 1.5, "color": "rgb(25, 25, 25)"}
    },
    "opacity": 0.6,
}]

my_layout = {
    "title": {"text": "Most-Starred Python Projects on GitHub", "font": {"size": 28}},
    "xaxis": {
        "title": {"text": "Repository", "font": {"size": 24}},
        "tickfont": {"size": 14},
    },
    "yaxis": {
        "title": {"text": "Stars", "font": {"size": 24}},
        "tickfont": {"size": 14},
    },
    "hoverlabel": {
        "bgcolor": "#E0E0E0"
    }
}

fig = {"data": data, "layout": my_layout}

html_path = os.path.join(ROOT_DIR, "data", "python_repos.html")

offline.plot(fig, filename = html_path)

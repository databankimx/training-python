"""Assignment 17.04"""
# Further Exploration: Visit the documentation for Plotly and either the GitHub API
#                      or the Hacker News API. Use some of the information you find
#                      there to either customize the style of the plots we've already made
#                      or pull some different information and create your own visualizations.
import os
import sys
import requests
from plotly import offline

ROOT_DIR = os.path.dirname(__file__)

# Pull the same GitHub data as before, but chart two numbers against each other
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
# An authenticated request gets a higher limit. See github-token-setup.md.
if os.environ.get("GITHUB_TRAINING_TOKEN"):
    headers["Authorization"] = f"Bearer {os.environ['GITHUB_TRAINING_TOKEN']}"
r = requests.get(url, headers=headers, timeout=10)
if r.status_code != 200:
    print(f"Failed to consume API!\n Status: {r.status_code}")
    sys.exit(-1)

repo_dicts = r.json()["items"]
names = [repo["name"] for repo in repo_dicts]
stars = [repo["stargazers_count"] for repo in repo_dicts]
forks = [repo["forks_count"] for repo in repo_dicts]

# Plotly's built-in dark template restyles the whole chart, and the colors show the star count
fig = {
    "data": [{
        "type": "scatter",
        "mode": "markers",
        "x": forks,
        "y": stars,
        "text": names,
        "marker": {
            "size": 14,
            "color": stars,
            "colorscale": "Viridis",
            "showscale": True,
            "colorbar": {"title": {"text": "Stars"}},
        },
    }],
    "layout": {
        "title": {"text": "Python Repositories: Stars against Forks", "font": {"size": 24}},
        "template": "plotly_dark",
        "xaxis": {"title": {"text": "Forks"}},
        "yaxis": {"title": {"text": "Stars"}},
    },
}

html_path = os.path.join(ROOT_DIR, "data", "python_repos_stars_forks.html")
offline.plot(fig, filename=html_path)

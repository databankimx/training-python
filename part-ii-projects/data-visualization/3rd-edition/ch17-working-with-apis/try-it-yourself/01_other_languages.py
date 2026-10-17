"""Assignment 17.01"""

# Other Languages: Modify the API call in python_repos.py so it generates a chart
#                  showing the most popular projects in other languages. Try languages
#                  such as JavaScript, Ruby, C, Java, Perl, Haskell, and Go.

import sys
from random import randint
import requests
import plotly.express as px

languages = ["javascript", "ruby", "c", "java", "perl", "haskell", "go"]
sel_lang = languages[randint(0, len(languages) - 1)]

print(f"Retrieving data for [{sel_lang}]...")

url = "https://api.github.com/search/repositories"
query_string = f"?q=language:{sel_lang}+sort:stars+stars:>10000"
request_url = url + query_string
headers = {"Accept": "application/vnd.github.v3+json"}

response = requests.get(request_url, headers=headers, timeout=10)
response_dict = response.json()

if response.status_code != 200:
    print(f"API connection to [{url}] failed\n\twith status code: {response.status_code}")
    sys.exit(-1)

repo_dicts = response_dict['items']

# Process the repo information
links, stars, hover_texts = [], [], []
for repo in repo_dicts:
    name = repo["name"]
    url = repo["html_url"]
    link = f"<a href='{url}'>{name}</a>"

    links.append(link)
    stars.append(repo["stargazers_count"])

    owner = repo["owner"]["login"]
    description = repo["description"]
    hover_text = f"{owner}<br>{description}"
    hover_texts.append(hover_text)

# Visualize
title = f"Most-Starred {sel_lang.title()} Projects on GitHub"
labels = {"x": "Repository", "y": "Stars"}
fig = px.bar(
    x=links, y=stars, title=title, labels=labels, hover_name=hover_texts,
    # Here, I am assigning "stars" as the color value and using a gradient for the bar colors
    color=stars, color_continuous_scale="Viridis"
)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
# This line hides the scale marker on the right hand side
fig.update(layout_coloraxis_showscale=False)

fig.show()

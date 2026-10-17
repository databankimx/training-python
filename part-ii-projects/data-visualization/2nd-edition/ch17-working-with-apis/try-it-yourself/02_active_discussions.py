"""Assignment 17.02"""
# Active Discussions: Using the data from hn_submissions.py, make a bar chart showing
#                     the most active discussions currently happening on Hacker News.
#                     The height of each bar should correspond to the number of
#                     comments each submission has. The label for each bar should
#                     include the submission's title and should act as a link to
#                     the discussion page for that submission.

import os
import sys
import requests
from plotly import offline

ROOT_DIR = os.path.dirname(__file__)
ITEM_COUNT = 20
MAX_RETRIEVE = 50

# Make an API call and store the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url, timeout=10)
if r.status_code != 200:
    print(f"Failed to consume API!\n Status: {r.status_code}")
    sys.exit(-1)

# Process information about each submission.
submission_ids = r.json()
links, titles, comments = [], [], []
for submission_id in submission_ids[:MAX_RETRIEVE]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url, timeout=10)
    response_dict = r.json()
    titles.append(response_dict["title"].split(")")[-1])
    links.append(
        f"<a href='http://news.ycombinator.com/item?id={submission_id}'>{response_dict['title']}")
    comments.append(response_dict["descendants"]
                    if "descendants" in response_dict.keys() else 0)

# A little sneaky sorting
comments, titles, links = zip(
    *sorted(zip(comments, titles, links), reverse=True))
comments, titles, links = comments[:ITEM_COUNT], titles[:ITEM_COUNT], links[:ITEM_COUNT]

# Make visualization.
data = [{
    "type": "bar",
    "x": links,
    "y": comments,
    "marker": {
        "color": "rgb(60, 100, 150)",
        "line": {"width": 1.5, "color": "rgb(25, 25, 25)"}
    },
    "opacity": 0.6,
    # "hovertext": titles
}]

my_layout = {
    "title": "Most Commented Posts on Hacker News",
    "titlefont": {"size": 28},
    "xaxis": {
        "title": "Post",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
    "yaxis": {
        "title": "Comments",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
    "hoverlabel": {
        "bgcolor": "#E0E0E0"
    }
}

fig = {'data': data, 'layout': my_layout}

html_path = os.path.join(ROOT_DIR, "Data", "hacker_news_posts.html")

offline.plot(fig, filename=html_path)

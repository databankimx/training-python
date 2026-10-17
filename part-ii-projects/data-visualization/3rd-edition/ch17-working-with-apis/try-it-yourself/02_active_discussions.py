"""Assignment 17.02"""

# Active Discussions: Using the data from hn_submissions.py, make a bar chart showing
#                     the most active discussions currently happening on Hacker News.
#                     The height of each bar should correspond to the number of comments
#                     each submission has. The label for each bar should include the
#                     submission's title and should act as a link to the discussion
#                     page for that submission.

import sys
from operator import itemgetter
import requests
import plotly.express as px

ITEM_COUNT = 25     # Number of items to display in the plot
# Can reduce this number for faster completion but with less accuracy
MAX_RETRIEVE = 500  # Number of top articles to retrieve data for

# Make an API call for a list of top articles, and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"

response = requests.get(url, timeout=10)

if response.status_code != 200:
    print(
        f"API connection to [{url}] failed\n\twith status code: {response.status_code}")
    sys.exit(-1)

submission_ids = response.json()
submission_dicts = []
# Get more info on first five submissions
for submission_id in submission_ids[:MAX_RETRIEVE]:
    # Call the API to get the specific article
    try:
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        response = requests.get(url, timeout=10)
    # pylint: disable=broad-except
    except Exception as e:
        input(e, "\nPress <ENTER> to continue...")
        continue

    if response.status_code != 200:
        print(
            f"API connection to [{url}] failed\n\twith status code: {response.status_code}")
        continue

    print("\033c", end="")
    print("ID:", submission_id)

    response_dict = response.json()

    # Build a dictionary for each article
    try:
        submission_dict = {
            "title": response_dict["title"],
            "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
            "comments": response_dict["descendants"]
        }
        submission_dicts.append(submission_dict)
    except KeyError:
        continue

submission_dicts = sorted(
    submission_dicts, key=itemgetter("comments"), reverse=True)

# Visualize
print("\033c", end="")
print("Visualizing...")
articles = [
    f"<a href='{d['hn_link']}' target='_blank'>{d['title']}</a>" \
    for d in submission_dicts][:ITEM_COUNT]
comments = [d["comments"] for d in submission_dicts][:ITEM_COUNT]
hover_texts = [d["title"] for d in submission_dicts][:ITEM_COUNT]
title = f"Top {ITEM_COUNT} Most Active Hacker-News Articles"
labels = {"x": "Article", "y": "Comments"}
fig = px.bar(
    x=articles, y=comments, title=title, labels=labels, hover_name=hover_texts,
    # Here, I am assigning "stars" as the color value and using a gradient for the bar colors
    color=comments, color_continuous_scale="Viridis"
)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)
# This line hides the scale marker on the right hand side
fig.update(layout_coloraxis_showscale=False)

fig.show()

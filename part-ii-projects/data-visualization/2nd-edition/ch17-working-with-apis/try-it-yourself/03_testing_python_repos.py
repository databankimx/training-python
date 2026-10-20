"""Assignment 17.03"""
# Testing python_repos.py: In `python_repos.py`, we printed the value of `status_code`
#                          to make sure the API call was successful. Write a program
#                          called test_python_repos.py that uses unittest to assert that
#                          the value of status_code is 200. Figure out some other
#                          assertions you can make — for example, that the number of
#                          items returned is expected and that the total number of
#                          repositories is greater than a certain amount.
import os
import sys
import unittest
import requests
from plotly import offline

def get_github_data(response_dict):
    """Process information about each submission."""
    ROOT_DIR = os.path.dirname(__file__)

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

def main():
    """Run the tests. unittest.main() searches __main__, which is the runner here, so load this module's tests directly."""
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(GithubTest)
    unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(suite)

class GithubTest(unittest.TestCase):
    """Unit tests for `python_repos.py`."""
    def test_data_retrieval(self):
        """Test that data is retrieved successfully."""
        # Make an API call and store the response.
        url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
        headers = {"Accept": "application/vnd.github.v3+json"}
        # An authenticated request gets a higher limit. See github-token-setup.md.
        if os.environ.get("GITHUB_TRAINING_TOKEN"):
            headers["Authorization"] = f"Bearer {os.environ['GITHUB_TRAINING_TOKEN']}"

        r = requests.get(url, headers=headers, timeout=10)
        self.assertEqual(r.status_code, 200)

        response_dict = r.json()
        self.assertEqual(len(response_dict["items"]), 30)
        self.assertGreater(response_dict["total_count"], 1000)

        get_github_data(response_dict)

if __name__ == "__main__":
    main()

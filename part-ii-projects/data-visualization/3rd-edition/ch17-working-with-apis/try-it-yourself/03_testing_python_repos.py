"""Assignment 17.03"""

# Testing python_repos.py: In python_repos.py, we printed the value of status_code
#                          to make sure the API call was successful. Write a program
#                          called test_python_repos.py that uses unittest to assert that
#                          the value of status_code is 200. Figure out some other
#                          assertions you can make — for example, that the number
#                          of items returned is expected and that the total number
#                          of repositories is greater than a certain amount.

import requests

def query_repos() -> requests.Response:
    """Get the list of repositories from the API"""
    url = "https://api.github.com/search/repositories"
    query_string = "?q=language:python+sort:stars+stars:>10000"
    request_url = url + query_string
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(request_url, headers=headers, timeout=10)
    assert response.status_code == 200, \
        f"API connection to [{url}] failed\n\twith status code: {response.status_code}"
    return response if response.status_code == 200 else None

def get_repo_data(response: requests.Response) -> list[dict]:
    """Parse the results and return a list of repository dictionaries"""
    if response is None or response.status_code != 200:
        return None
    response_dict = response.json()
    if "items" in response_dict:
        items = response_dict["items"]
        assert len(items) > 20, f"Only received {len(items)} items!"
        return items
    return None

def display_data(repo_dicts: list[dict]) -> None:
    """Print repository information"""
    print("\nSelected information about each repository:")

    for repo_dict in repo_dicts:
        assert repo_dict['stargazers_count'] > 10000, \
            f"{repo_dict['name']}: {repo_dict['stargazers_count']} stars!"
        print(f"Name: {repo_dict['name']}")
        print(f"- Owner: {repo_dict['owner']['login']}")
        print(f"- Stars: {repo_dict['stargazers_count']}")
        print(f"- Repository: {repo_dict['html_url']}")
        print(f"- Description: {repo_dict['description']}\n")

def main():
    """Main function"""
    response = query_repos()
    data = get_repo_data(response)
    display_data(data)

if __name__ == "__main__":
    main()

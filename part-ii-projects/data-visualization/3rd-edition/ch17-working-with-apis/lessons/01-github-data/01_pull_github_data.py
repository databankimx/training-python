"""Lesson 1.1 - GitHub Data"""

import sys
# We use the requests library to perform API calls over the internet.
import requests
# > python -m pip install requests

# We are going to connect to the API exposed by GitHub
# Reference:    https://docs.github.com/en/rest
url = "https://api.github.com/search/repositories"
# We will search for repositories using python with greater than 10K stars,
#     sorted by number of stars.
query_string = "?q=language:python+sort:stars+stars:>10000"
# Combine the base URL and query string to get the full request URL
request_url = url + query_string

# We use a dictionary to define the headers we will include in the request.
#     Not all APIs require the same headers.
headers = {"Accept": "application/vnd.github.v3+json"}

# We'll make a request to our URL with the specified headers
response = requests.get(request_url, headers=headers, timeout=10)

# Assuming we were successful, the HTTP response code should be 200
print(f"Status code: {response.status_code}")

response_dict = response.json()

# Check to see if the request succeeded

if response.status_code != 200:
    print(f"API connection to [{url}] failed\n\twith status code: {response.status_code}")
    sys.exit(-1)
elif "message" in response_dict:
    # Otherwise, there may be "message" and "errors" keys in the response dictionary
    print("Error:", response_dict["message"])
else:
    print(f"Success:\n - Total repositories: {response_dict['total_count']}")

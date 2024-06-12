import requests
from requests.auth import HTTPBasicAuth


# Configuration settings
username = "theurbanpenguin"
token = "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"  # Generate a personal access token from GitHub
api_url = "https://api.github.com/user/repos"

# API request to list repositories
response = requests.get(api_url, auth=HTTPBasicAuth(username, token))

if response.status_code == 200:
    repos = response.json()
    print("Repositories:")
    for repo in repos:
        print(f"- {repo['name']}")
else:
    print(f"Failed to list repositories. Status code: {response.status_code}")
    print(response.json())
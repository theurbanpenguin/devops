import requests
from requests.auth import HTTPBasicAuth

# Configuration settings
username = "theurbanpenguin"
token = "ghp_im83xx11iCcWQwM"  # This will be deleted
repo_name = "new-repo"
api_url = "https://api.github.com/user/repos"

# API request to create a repository
response = requests.post(
    api_url,
    json={"name": repo_name},
    auth=HTTPBasicAuth(username, token)
)

if response.status_code == 201:
    print(f"Repository '{repo_name}' created successfully.")
else:
    print(f"Failed to create repository. Status code: {response.status_code}")
    print(response.json())
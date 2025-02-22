import os
import json
import requests
import re

# File containing the JavaScript data (update the path if necessary)
data_file = "data.js"

# Directory to save downloaded repositories
download_dir = "github_repos"
os.makedirs(download_dir, exist_ok=True)


def extract_github_urls(js_file):
    """Extract GitHub repository URLs from the data.js file."""
    with open(js_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Regex to find URLs in JSON-like structure
    url_pattern = re.findall(r"https://[\w.-]+\.github\.io/[\w-]+", content)

    # Transform GitHub Pages URLs to Repository URLs
    repo_urls = []
    for url in url_pattern:
        match = re.match(r"https://([\w-]+)\.github\.io/([\w-]+)", url)
        if match:
            username, repo_name = match.groups()
            repo_urls.append(f"https://github.com/{username}/{repo_name}")

    return list(set(repo_urls))  # Remove duplicates if any


def download_github_repo(repo_url):
    """Download GitHub repository as a ZIP file."""
    repo_name = repo_url.strip("/").split("/")[-1]
    zip_url = f"{repo_url}/archive/refs/heads/main.zip"  # Assumes 'main' branch

    try:
        response = requests.get(zip_url, stream=True)
        response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)

        zip_path = os.path.join(download_dir, f"{repo_name}.zip")
        with open(zip_path, "wb") as zip_file:
            for chunk in response.iter_content(chunk_size=1024):
                zip_file.write(chunk)

        print(f"Downloaded: {repo_name}.zip")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download {repo_name}: {e}")


# Extract GitHub repository URLs from data.js
repo_urls = extract_github_urls(data_file)

# Download each repository
for repo_url in repo_urls:
    download_github_repo(repo_url)

print("Download process completed.")

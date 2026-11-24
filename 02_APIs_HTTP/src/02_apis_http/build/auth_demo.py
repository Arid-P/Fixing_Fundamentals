import os
from dotenv import load_dotenv

from fetcher_core import fetch_json

load_dotenv()
token = os.getenv("GITHUB_TOKEN")

url = "https://api.github.com/user"
headers = {"User-Agent": "Auth-Demo"}
if token is not None:
    headers["Authorization"] = f"Bearer {token}"
payload = fetch_json(url=url, headers=headers)


print("Authenticated as:", payload["login"])  # type: ignore

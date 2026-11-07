from os import getenv
from dotenv import load_dotenv
from requests import get
from datetime import datetime as dt

from icecream import ic

ic.disable()

url = r"https://api.github.com/rate_limit"
headers = {"User-Agent": "Ari-Test"}


def limits_print() -> None:
    global headers
    resp = get(url, headers=headers)

    time_diff = (dt.fromtimestamp(float(resp.headers.get("X-RateLimit-Reset"))) - dt.now()).seconds  # type: ignore

    days = int(time_diff / (60 * 60 * 24))
    time_diff %= 24 * 60 * 60
    hours = int(time_diff / (60 * 60))
    time_diff %= 60 * 60
    mins = int(time_diff / 60)
    time_diff = 60
    sec = int(time_diff)

    times = [
        f"{str(days) + " days " if days else ""}",
        f"{str(hours) + " hours " if hours else ""}",
        f"{str(mins) + " mins " if mins else ""}",
        f"{str(sec) + " sec " if sec else ""}",
    ]

    print(
        f"Rate Limit: {resp.headers.get("X-RateLimit-Limit")} ;",
        f"Rate Limit Rmaining: {resp.headers.get("X-RateLimit-Remaining")} ;",
        f"Rate Limit Reset: {resp.headers.get("X-RateLimit-Reset")} ;",
        f"Reset time in dateime: {''.join(times)}",
        sep="\n",
    )


print("No auth test")
limits_print()

# loadinbg token
load_dotenv()
token = getenv("GITHUB_TOKEN")

print("\nAuth test")
headers = {"User-Agent": "Ari-Test", "Authorization": f"Bearer {token}"}
ic(headers)
limits_print()

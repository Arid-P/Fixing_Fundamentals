import time
import requests
import logging
from sys import exit
from typing import Any
from datetime import datetime as dt, timezone

from icecream import ic

from utilis import get_logger, api_failure_handler
from cache import get_cached_repos, get_cached_repos_stats, update_cache, save_summary

logger: logging.Logger = get_logger(__name__)


def _wait(retry: int) -> None:
    wait_time = 2**retry
    print(f"Waiting for {wait_time} seconds.", end=" ", flush=True)

    time.sleep(wait_time)
    print("Retrying")


def _fetch(
    url: str,
    params: dict | None = None,
    headers: dict | None = None,
) -> dict[str, Any]:
    max_retries: int = 3
    timeout: float = 5.0

    # to keep them in bound
    resp: requests.Response = requests.Response()
    data = requests.Response()
    err: (
        requests.ConnectionError
        | requests.Timeout
        | requests.HTTPError
        | requests.JSONDecodeError
        | None
    ) = None

    with requests.Session() as session:
        for retry in range(max_retries):
            try:
                resp = session.get(url, headers=headers, params=params, timeout=timeout)

                resp.raise_for_status()
                data = resp.json()
                break
            except (requests.ConnectionError, requests.Timeout) as e:
                err = e
                if retry != max_retries - 1:
                    _wait(retry)

            except requests.HTTPError as e:
                err = e
                if resp.status_code in [401, 403, 404, 429]:
                    break

            except requests.JSONDecodeError as e:
                err = e
                data = None
                break

    return {
        "status code": resp.status_code,
        "error": err,
        "request": resp.request,
        "headers": resp.headers,
        "body": resp.text,
        "data": data,
    }


def _rate_limits(headers: dict[str, str]) -> dict[str, str]:
    url = r"https://api.github.com/rate_limit"

    payload: dict[str, Any] = _fetch(url=url, headers=headers)
    _, error = api_failure_handler(api_payload=payload)

    if error:
        logger.info("Some error in rate limti calulation")
        logger.debug("The payload: %s", payload)

        print("Some internal error has occured")

    time_diff = (dt.fromtimestamp(float(payload["headers"].get("X-RateLimit-Reset"))) - dt.now()).seconds  # type: ignore

    days = int(time_diff / (60 * 60 * 24))
    time_diff %= 24 * 60 * 60
    hours = int(time_diff / (60 * 60))
    time_diff %= 60 * 60
    mins = int(time_diff / 60)
    time_diff %= 60
    sec = int(time_diff)

    times = [
        f"{str(days) + " days " if days else ""}",
        f"{str(hours) + " hours " if hours else ""}",
        f"{str(mins) + " mins " if mins else ""}",
        f"{str(sec) + " sec " if sec else ""}",
    ]

    return {
        "total": payload["headers"].get("X-RateLimit-Limit"),
        "amount left": payload["headers"].get("X-RateLimit-Remaining"),
        "time left": "".join(times),
        "rl-reset": f"Rate Limit Reset: {payload["headers"].get("X-RateLimit-Reset")} ;",
    }


def _process_lang(langs: dict[str, int]):
    total = sum(langs.values())
    uf_langs: list[tuple[str, float]] = []

    for key, val in langs.items():
        uf_langs.append((key, int(val) / total * 100))

    return dict(sorted(uf_langs, key=lambda el: -el[1]))


def _stats_repo(
    username: str,
    repos: dict[str, Any],
    recent_count: int,
    headers: dict[str, str],
) -> tuple[list[Any], dict[str, int]]:
    # Since only 3 arguments will be there in reponse no need for pagination
    # This runs when caching isnt suitbale, ie, cache = False

    now = dt.now(timezone.utc)
    logger.info("Fetching the language stats for the user's repos")
    logger.debug("user: %s", username)

    stats_payload = []
    languages: dict[str, int] = {}

    for repo in repos["response"][0:recent_count]:
        url: str = f"https://api.github.com/repos/{username}/{repo["name"]}/languages"

        logger.debug("The api url: %s", url)

        api_payload = _fetch(url=url, headers=headers)
        _, error = api_failure_handler(
            api_payload=api_payload, payload={"cache": False}
        )

        logger.info("Got the api payload back")
        logger.debug("The payload's data: %s", api_payload)

        if error:
            logger.info("Exiting the program. (Check the apifailure_handler function)")
            exit("Some error has occured internally")

        untouched = (now - repo["pushed"]).days > 90

        lang = api_payload["data"]
        if len(lang) <= 0:
            stats_payload.append(
                {
                    "name": repo["name"],
                    "language": None,
                    "stars": repo["stars"],
                    "untouched": untouched,
                }
            )
        else:
            stats_payload.append(
                {
                    "name": repo["name"],
                    "language": list(lang.keys())[0],
                    "stars": repo["stars"],
                    "untouched": untouched,
                }
            )

            for key, val in lang.items():
                if key not in languages:
                    languages[key] = val
                else:
                    languages[key] += val

    return stats_payload, languages


def _user_repos(username: str, headers: dict[str, str]) -> dict[str, Any]:
    # making the request
    logger.info("Fetching all the users repos")
    repo_payload: dict[str, Any] = {
        "user": username,
        "cache": False,
        "etag": "",
        "response": [],
    }

    url: str = f"https://api.github.com/users/{username}/repos"
    params: dict[str, Any] = {
        "per_page": 100,
        "sort": "pushed",
        "direction": "desc",
        "page": 1,
    }

    logger.debug("The api url: %s", url)

    first = True
    while True:
        logger.debug("The query parameters for api call: %s", params)
        api_payload = _fetch(url=url, params=params, headers=headers)
        repo_payload, _ = api_failure_handler(
            api_payload=api_payload, payload=repo_payload
        )

        if first:
            repo_payload["etag"] = api_payload["headers"].get("etag")

            if repo_payload["cache"] and first:
                return repo_payload
            first = False

        # processing the payload
        for repo in api_payload["data"]:
            repo_payload["response"].append(
                {
                    "name": repo.get("name"),
                    "stars": repo.get("stargazers_count"),
                    "pushed": dt.fromisoformat(repo["pushed_at"]),
                    "forked": repo.get("fork"),
                }
            )

        if api_payload["headers"].get("Link") and (
            "next" in api_payload["headers"].get("Link")
        ):
            params["page"] += 1

            if headers.get("etag"):
                del headers["etag"]
        else:
            break

    return repo_payload


def get_payload(
    username: str, recent_count: int, token: str | None
) -> dict[str, dict[str, Any]]:
    cache_repo: dict[str, Any] = get_cached_repos()

    headers: dict[str, str] = {
        "User-Agent": "GH-Activity",
        "Accept": "application/vnd.github+json",
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"
    if len(cache_repo) > 0:
        if cache_repo["etag"]:
            headers["If-None-Match"] = cache_repo["etag"]

    all_repos: dict[str, Any] = _user_repos(username=username, headers=headers)

    if all_repos["cache"]:  # when cache is needed
        if len(cache_repo) <= len(all_repos):
            # Cache is missing field, ie, is incomplete
            exit("Cache is not available and data could be retrieved through API")
        elif cache_repo["user"] == username:
            cache_stat: dict[str, dict[str, Any]] = get_cached_repos_stats()
            output_data = {
                "repos": cache_repo,
                "stats": cache_stat["stats"],
                "lang_stats": cache_stat["lang_stats"],
            }
            output_data["rate_limits"] = {}
        else:
            exit(f"User not found. No user exists with the name: {username}")

    else:  # When cache is useless
        stats_repo, languages = _stats_repo(
            username=username,
            repos=all_repos,
            recent_count=recent_count,
            headers=headers,
        )

        lang_stats: dict[str, float] = _process_lang(languages)

        output_data = {
            "repos": all_repos,
            "stats": {"stats": stats_repo},
            "lang_stats": {"languages": lang_stats},
        }

        ci = 0
        while ci < 3:
            if update_cache(output_data):
                break
            ci += 1
        else:
            logger.info("Caching the data failed several time, and was not possible")
            print("Could not cache the data")

        output_data["rate_limits"] = _rate_limits(headers=headers)

    return output_data


def user_summary(username: str, information: dict[str, dict[str, Any]]) -> None:
    summary = {
        "user": username,
        "generated_at": dt.now(timezone.utc),
        "total_repos": len(information["repos"]["response"]),
        "total_stars": sum(
            [int(repo["stars"]) for repo in information["repos"]["response"]]
        ),
        "untouched_repos_90_days": list(
            map(
                lambda stat: stat["name"],
                filter(lambda x: x["untouched"], information["stats"]["stats"]),
            )
        ),
        "top_languages": dict(
            sorted(
                information["lang_stats"]["languages"].items(),
                key=lambda item: -item[1],
            )[:5]
        ),
        "rate_limit_remaining": (
            information["rate_limits"]["amount left"]
            if information["rate_limits"] else "Cached used"
        ),
    }

    tr = 0
    while tr < 3:
        logger.info("Try %s: Wrting the summary", tr)
        status = save_summary(summary=summary)
        if status:
            break
        tr += 1
    else:
        logger.info("Could nto wrtin gthe user summary")

    return


def main() -> None:
    """It is the starting function. From it you can understand a basic flow of the whole program"""
    headers: dict[str, str] = {
        "User-Agent": "GH-Activity",
        "Accept": "application/vnd.github+json",
    }

    ic(_rate_limits(headers=headers))
    print(get_payload("Arid-P", 10, None))
    print(_fetch("https://httpbin.org/status/200"))


if __name__ == "__main__":
    main()

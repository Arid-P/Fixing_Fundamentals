# Design: GitHub Activity Report (gh_report)

## Purpose (2 sentences)
A CLI tool to view a user's public repos, and the report of the most recently pushed repos 

## Inputs / Outputs
1. We will use `argprase` library to initially process the arguments provided when running the script, `python gh_report.py <args>` in CLI. But if no argument is provided or some are missing or invalid then we prompt the user for it as told in [1 of Failure Modes and Handling](#failure-modes-and-handling).

2. The user has main 3 tasks he can choose: `information` with flag `-i` or `-I` or `--info`, `GitHub Token` with flag `-t` or `-T` or `--token`, and `exit`, this will only be available when the user runs the scripts with no arguments, more details in [2 of Failure Modes and Handling](#failure-modes-and-handling).

3. For `information` task, the user needs to provide two inputs: `user` and `N`. `user` is for which user's repo do we have to display in the `public repo table`. `recent_count` is the number most recent repos that the script needs to process for the `stats table`. [3 and 4 of Failure](#failure-modes-and-handling), [For Tables](#h-table-and-summary-json-layout)

4. If the user provided `Github Token` flag then a path will be the input with it. The path will be for the `.env` file. We copy the .env file to the programs personal directory (like how commands are saved in a directory), and check if the copied file and the given file have the same key, if no then recopy. If yes then we empty the original file. Emptying is always last. [5 of Failure Modes and Handling](#failure-modes-and-handling)

5. The `public repo table` will be printed by `display_public_repo_table` function. It displays all the public repos of the provided user. The layout of the table is:
    |S.No.|Name|Stars|Last Pushed|Forked?|
    |---|---|---|---|---|
    |1.|...|...|...|Yes|
    |2.|...|...|...|No|

6. The `stats table` will be printed by `display_stats_table` function. It displays the stats of the `recent_count` most recent repos pushed. The layout is:
    |S.No.|Full Name|Language|Stars|Untouched|
    |---|---|---|---|---|
    |1.|...|...|...|Yes|
    |2.|...|...|...|No|

7. The `lang stat table` will be displayed by `display_lang_stat_table` function. It displays the languages used in `stats table` in order by % of total bytes. The layout is:
    |S.No.|Language|% of total bytes|
    |---|---|---|
    |1.|...|...|
    |2.|...|...|

8. Finally, the rate limit of the user will be displayed. It will be done by `display_rate_limit`. The format is like:
    ```text
    Total Rate Limit: ...
    Rate Limit Used: ...
    Time left till limit Resets: ...
    ```

## States and transitions (diagram or table)

## Modules and interfaces (who calls whom, with what data)
- For API details [Read API Reference](/02_APIs_HTTP/ai_nd_report/GITHUB_API_REFERENCE.md)

- We will have the following files:
    - `main.py`
    - `cli.py` (name requires work)
    - `processing.py`
    - `cache.py`
    - `utilis.py`

- The `main` file will how the `GitHub Token` and will pass it to `processing` functions.
- The `argprase` will be established in `main.py`, and will be passed as an argument in `cli.py` files' input functions.

- The `cli` will have 2 main input functions. All of them will return a python `dictionary`.  
    The main are:
    - `args_input` which will process the inputs that are received by CLI. If it returns an empty dict, then we call the next function.
    - `prompt_input` it will simply prompt the user to select what task he/she wants, then take input for the action. Here, the `exit` option will be shown.

- The `cli` file will contain the 4 displaying function. They will return nothing, but will take he processed data which can be used directly to print the table.
    - `display_public_repo_table`
    - `display_stats_table`
    - `display_lang_stat_table`
    - `display_rate_limit`

- The `processing` file will have all the functions that will call the API and process its output. The `fetch_json` function will be here, and its architecture will be updated to: 
    ```python
    def fetch(
        url: str,
        params: dict | None = None,
        headers: dict | None = None,
    ) -> dict:

        max_retries: int = 3
        timeout: float = 5.0
        ...
    ```
    And it will return something like:
    ```python
    return {
        "status code": resp.status_code,
        "error": err,
        "header": resp.headers,
        "data": data,
    }
    ```

> Side Note: The `fetcher_core.py` will be renamed to `processing.py` and the function will be renamed to `fetch`.

- The `processing` will have 3 functions. Each of them will have their own URL, parameters, and headers which they will send to `fetch`. But the `GitHub Token` will be `global`. 
    ```python
    headers = {
        "User-Agent": "Ari-Test",
        "Authorization": f"Bearer {github_token}",
        "If-None-Match": <etag>
    }
    ```

- These functions are:
    - `rate_limit_process`, it returns a `dict` like
        ```json
        {
            "error": ...,
            "total limit": ..., # <int>
            "limit left": ..., # <int>
            "reset_time": ..., # <str>, times variable given below
            "reset_original": ... # the exact time in response
        }
        ```
        ```python
        times = [
            f"{str(days) + " days " if days else ""}",
            f"{str(hours) + " hours " if hours else ""}",
            f"{str(mins) + " mins " if mins else ""}",
            f"{str(sec) + " sec " if sec else ""}",
        ]
        ```
    - `user_repos`, it accesses all the repos of a user sorted by `pushed` field in descending order (`desc`). It returns:
        ```json
        {
            "error": ...,
            "repos": [
                {
                    "full name": resp['full_name'],
                    "name": resp['name'],
                    "stars": resp['stargazers_count'],
                    "pushed": resp['pushed_at'], # <ISO 8601>
                    "forked": resp['fork']
                }
            ]
        }
        ```
    - `stats_process`, it fetches the most recent repos' stats for the given `user`. It takes the output of `user_repos` function as one of its arguments, and works upon it. It returns:
        ```json
        {
            "error": ...,
            "full_name": ...,
            "language": ...,
            "stars": ...,
            "untouched": ...,
            "lang_stats": {
                <lang_name>: ...,
            }
        }
        ```

- In all above functions, there is `error` field. Before moving to output we first need to check if it is `None` or not. If yes then proceed, otherwise we exit the program with the error being gracefully shown to user.

- The `utitiles` will hold code for things like logger, input validation function.

- The `cache.py` file will manage all the functions that read or write on the cache files. In the script file's parent folder we will create data/cache/ and store the cache files there.

## Constraints (time, memory, hardware, cost)
- Rate limits: 60 req/hr (unauthenticated) vs 5,000 req/hr (authenticated).
- Network timeout: 5.0 seconds per request.
- Max retries: 3 attempts with exponential back off on transient errors (connection/timeouts).
- Memory & Disk: Cache stored locally on disk under `data/cache/`

## Failure modes and handling
1. **No arguments in CLI:** Then we have a proper input function that inputs which option does the user want (`information`, `GitHub Token`, `exit`).

2. **`exit` Task Option:** When we prompt the user for input, like above, we will also provide an exit option since the user has run the script without any arguments so it may be a mistake. 

3. **`user` Missing in `-i` flag:** If not provided we exit with message telling that no username was provided.

4. **`recent_count` Missing in `-i` flag:** If this isn't provided then we just don't display the stats table instead we display the message that since no number of most recent was provided the table wasn't displayed.

5. **Path in -T flag is missing:** If the path is missing we give the error that no path was provided  and exit the program. 

## Test plan (how I will know it works)
We will implement `pytest` for testing. Since our codebases is based on functional programming, we will have tests for each function.

---

## Specific Design Questions

#### (a) What does the fetch layer return now, since fetch_json returns only JSON but this tool needs headers? 
- It returns a dictionary containing status code, error, headers, and the parsed JSON data:
  ```python
  {
      "status code": resp.status_code,
      "error": err,
      "header": resp.headers,
      "data": data,
  }
  ```

#### (b) What stops the pagination loop and what caps the repo count?
- We check the `Link` header in response headers to see if `Link` is present and if `rel="next"` is present. If `Link` is absent or `rel="next"` is not in it, the pagination loop stops.

#### (c) Rate-limit policy and what the user sees
- If the rate limit is exhausted (remaining = 0), we notify the user with the reset time in local time, and prompt whether they want the program to sleep for the remaining duration or exit cleanly.

#### (d) Cache key, what is stored (body, ETag, time), and where the file lives with the path anchored to the file
- The `cache.py` file will manage all the functions that read or write on the cache files. In the script file's parent folder we will create `data/cache/` and store the cache files there.

#### (e) Error-to-message table
|Status Code|Error|What to show to User|
|---|---|--|
|`401`|`HTTPError`|"Invalid GITHUB_TOKEN provided in .env."|
|`403` or `429`|`HTTPError`|"Rate limit exceeded. Reset at {local_time}."|
|`404`|`HTTPError`|"Error: User '{username}' does not exist on GitHub."|
|None|`ConnectionError` or `Timeout`|"Network error: Could not reach GitHub API. Falling back to offline cache if available."|
|`200`|`JSONDecodeError`|"Error: Received malformed response from server."|
|None|`ValueError`|"Value Error: The provided value ({value}) doesn't match the required format ({data type})"|

#### (f) Where the token is read and what happens if it is missing
- The `main` file will how the `GitHub Token` and will pass it to `processing` functions.

#### (g) Call cost for a user with N repos
For a user with $N_{\text{repos}}$ total public repositories, requesting language statistics for the $K$ most recently pushed repositories:

1. **Fetching All Repositories (with pagination):**
   Using GitHub's maximum allowed page size ($\text{per\_page} = 100$):
   $$\text{Calls}_{\text{repos}} = \left\lceil \frac{N_{\text{repos}}}{100} \right\rceil$$

2. **Fetching Languages for Top $K$ Repositories:**
   One endpoint request per repository:
   $$\text{Calls}_{\text{languages}} = K$$

3. **Rate Limit Status Check:**
   $$\text{Calls}_{\text{rate\_limit}} = 1$$

- **Total API Calls (Cold Cache / First Run):**
  $$\text{Total Calls} = 1 + \left\lceil \frac{N_{\text{repos}}}{100} \right\rceil + K$$
- **Primary Rate-Limit Cost with Cached ETags (`304 Not Modified`):**
  $$\text{Rate-Limit Cost} = 0$$
  *(GitHub consumes 0 core rate-limit quota when returning `304 Not Modified`)*.

#### (h) Table and summary JSON layout
- **`public repo table`:** It is the table that lists all the repos of a user. The format is like:
    |S.No.|Name|Stars|Last Pushed|Forked?|
    |---|---|---|---|---|
    |1.|...|...|...|Yes|
    |2.|...|...|...|No|

    In caching, we directly save the received response but with tine like:
	```json
	{
		"time": <datetime_object>,
        "etag": resp['etag'],
		"response": <response_received>
	}
	```	

- **`stats tables`:** It is the table that lists the `recent_count` most recent repos pushed. The format is like:
    |S.No.|Full Name|Language|Stars|Untouched|
    |---|---|---|---|---|
    |1.|...|...|...|Yes|
    |2.|...|...|...|No|

    In caching, the JSON schema is like:
    ```json
    {
		"time": <datetime_object>,
        "etag": resp['etag'],
        "stats": {
            <full_name>: {
                "language": ...,
                "stars": ...,
                "untouched": ...
            },
            ...
        }
    }
    ```

- **`lang stat table`:** It is the table that list the languages used in the `stats table` with top languages by % of total bytes. The format is:
    |S.No.|Language|% of total bytes|
    |---|---|---|
    |1.|...|...|
    |2.|...|...|

    In caching, the JSON schema is like:
    ```json
    {
        "time": <datetime_object>,
        "etag": resp['etag'],
        "stats": {
            "language": <% of total bytes>,
            ...
        }
    }
    ```

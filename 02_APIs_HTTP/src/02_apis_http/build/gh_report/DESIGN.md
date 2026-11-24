# Design: GitHub Activity Report (gh_report)

## Purpose (2 sentences)
A CLI tool to view a user's public repos, and the report of the most recently pushed repos 

## Inputs / Outputs
1. We will use `argprase` library to initially process the arguments provided when running the script, `python gh_report.py <args>` in CLI. But if no argument is provided or some are missing or invalid then we prompt the user for it as told in [1 of Failure Modes and Handling](#failure-modes-and-handling).

2. The user has main 3 tasks he can choose: `information` with flag `-i` or `-I` or `--info`, `GitHub Token` with flag `-t` or `-T` or `--token`, and `exit`, this will only be available when the user runs the scripts with no arguments, more details in [2 of Failure Modes and Handling](#failure-modes-and-handling). We will also have the flags: `-n`, `-N`, `N` for the number of most recently pushed repos for the variable `recent_count`.

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

```text
[Start: main.py]
       │
       ▼
[CLI / Prompt Input (cli.py)]
   ├─► TaskType.EXIT  ──► [Clean Exit]
   ├─► TaskType.TOKEN ──► [establish_env_token() in main.py]
   └─► TaskType.INFORMATION
              │
              ▼
       [Load Token (paths.py / data/.env)]
              │
              ▼
       [get_payload() in processing.py]
              │
              ├─► [_rate_limits(): fetch /rate_limit]
              │
              ├─► [_user_repos(): fetch /users/{username}/repos]
              │      └─► Page 1 ETag validation (If-None-Match)
              │      └─► 304 Not Modified: Reuse cached repos
              │      └─► 200 OK: Pagination loop following Link: rel="next"
              │
              ├─► [_stats_process(): for top N recent repos]
              │      └─► fetch /repos/{owner}/{repo}/languages
              │      └─► Check 90+ days untouched
              │
              └─► [_lang_stats(): aggregate % of total bytes]
              │
              ▼
       [Cache Update (cache.py)]
              └─► Atomic write via .tmp & .backup to data/cache/
                     ├─► repos.json
                     ├─► stats.json
                     └─► lang_stats.json
```

## Modules and interfaces (who calls whom, with what data)
- For API details [Read API Reference](/02_APIs_HTTP/ai_nd_report/GITHUB_API_REFERENCE.md)

- **Package Architecture (`src/gh/`):**
    - `paths.py`: Anchors all paths (`log_file`, `env_path`, `cache_dir`, `cache_files`) to project root `gh_report/data/` using `Path(__file__).resolve()`.
    - `utilis.py`: Logging (`setup_logging`, `get_logger`), `TaskType` enum, CLI validators (`int_valid`, `path_valid`), and `api_failure_handler`.
    - `cli.py`: Parses CLI flags (`-i`, `-n`, `-t`) via `argparse` or prompts interactively via `_prompt_input()`.
    - `processing.py`: Resilient HTTP client (`_fetch()`), pagination, repo stats calculation, language percentage aggregation, and rate limit inspection.
    - `cache.py`: Manages reading and atomic disk caching with backups (`.tmp` -> `.backup` -> active `.json`).
    - `main.py`: Entrypoint orchestrating CLI input, environment token configuration, and payload generation.

- **Data Flow:**
    1. `main.py` invokes `cli.cli_input()`, returning `{"todo": TaskType, ...}`.
    2. If `TaskType.TOKEN`: `establish_env_token()` safely copies the provided `.env` to `gh_report/data/.env`.
    3. If `TaskType.INFORMATION`: `main.py` calls `processing.get_payload(username, recent_count, token)`.
    4. `processing._fetch()` executes HTTP requests with a 5.0s timeout and exponential backoff retry on transient errors (ConnectionError, Timeout).
    5. `_user_repos()` checks Page 1 `ETag`. If 304, reuses disk cache; if 200, iterates over all pages using `params["page"] += 1` while `rel="next"` is in the `Link` header.
    6. `_stats_process()` requests `/languages` for the top $N$ recent repos and computes `untouched` status (`pushed_at >= 90 days`).
    7. `_lang_stats()` aggregates bytes across all returned languages and computes individual percentages of total bytes.
    8. `cache.update_cache()` writes `repos.json`, `stats.json`, and `lang_stats.json` atomically with backups.
    9. `processing.summary_generator()` aggregates the summary metrics and saves them to `data/output/summary_<user>.json`.
    10. `cli.cli_output()` renders styled `rich` tables and panels for all 4 sections in the terminal.

- The `processing` file defines functions that manage specific API requests and data transformations:
    - `_fetch(url, params, headers)`: Core HTTP helper with 3 retries, exponential backoff, and 5.0s timeout.
    - `_rate_limits(headers)`: Calls `/rate_limit`, returning `rate-limit`, `rl-left`, `rl-reset`, and `rl-rest-time`.
    - `_user_repos(username, token, etag, params)`: Fetches user repositories with pagination and ETag validation.
    - `_stats_process(username, repos, recent_count, headers)`: Gathers language bytes per repo and calculates 90-day untouched state.
    - `_lang_stats(repos_stats)`: Computes individual language percentages of total code bytes across the top repos.
    - `get_payload(username, recent_count, token)`: Master pipeline returning `{repos, stats, lang_stats, rate_limits}`.
    - `summary_generator(information)`: Builds the summary dictionary and writes `summary_<user>.json`.

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

4. **`recent_count` Missing in `-i` flag:** If this isn't provided then we just suppose the `recent_count` to be $5$.

5. **Path in -T flag is missing:** If the path is missing we give the error that no path was provided and exit the program. 

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
        "stats": [
            {
                "name": <full_name>,
                "language": ...,
                "stars": ...,
                "untouched": ...
            },
            ...
        ]
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
        "stats": {
            "language": <% of total bytes>,
            ...
        }
    }
    ```

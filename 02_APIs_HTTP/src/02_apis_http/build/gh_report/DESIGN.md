# Design: GitHub Activity Report (gh_report)

## Purpose (2 sentences)
A CLI tool to view a user's public repos, and the report of the most recently pushed repos 

## Inputs / Outputs
1. We will use `argprase` library to initially process the arguments provided when running the script, `python gh_report.py <args>` in CLI. But if no argument is provided or some are missing or invalid then we prompt the user for it as told in [1 of Failure Modes and Handling](#failure-modes-and-handling).

2. The user has main 3 tasks he can choose: `information` with flag `-i` or `-I` or `--info`, `GitHub Token` with flag `-t` or `-T` or `--token`, and `exit`, this will only be available when the user runs the scripts with no arguments, more details in [2 of Failure Modes and Handling](#failure-modes-and-handling).

3. For `information` task, the user needs to provide two inputs: `user` and `N`. `user` is for which user's repo do we have to display in the `public repo table`. `recent_count` is the number most recent repos that the script needs to process for the `stats table`. [3 and 4 of Failure](#failure-modes-and-handling), [For Tables](#h-table-and-summary-json-layout)

4. If the user provided `Github Token` flag then a path will be the input with it. The path will be for the ".env" file. We copy the .env file to the programs personal directory (like how commands are saved in a directory), and check if the copied file and the given file have the same key, if no then recopy. If yes then we empty the original file. Emptying is always last.

5. The "public repo table" will be printed by "display_public_repo_table" function. It displays all the public repos of the provided user. The layout of the table is:
    |S.No.|Name|Stars|Last Pushed|Forked?|
    |---|---|---|---|---|
    |1.|...|...|...|Yes|
    |2.|...|...|...|No|

6. The "stats table" will be printed by "display_stats_table" function. It displays the stats of the `recent_count` most recent repos pushed. The layout is:
    |S.No.|Full Name|Language|Stars|Untouched|
    |---|---|---|---|---|
    ||1.|...|...|...|Yes|
    |2.|...|...|...|No|

7. The "lang stat table" will be displayed by "display_lang_stat_table" function. It displays the languages used in "stats table". The layout is:
    |S.No.|Language|Number of repo used in|
    |---|---|---|
    ||1.|...|...|
    |2.|...|...|

8. Finally the rate limit of the user will be displayed. It will be done by "display_rate_limit". The fornat is like:
		```text
		Total Rate Limit: ...
		Rate Limit Used: ...
		Time left till limit Resets: ...
		```


## States and transitions (diagram or table)

## Modules and interfaces (who calls whom, with what data)

## Constraints (time, memory, hardware, cost)

## Failure modes and handling
1. **No arguments in CLI:** Then we have a proper input function that inputs which option does the user want (`information`, `GitHub Token`, `exit`).

2. **`exit` Task Option:** When we prompt the user for input, like above, we will also provide an exit option since the user has run the script without any arguments so it may be a mistake. 

3. **`user` Missing in `-i` flag:** If not provided we exit with message telling that no username was provided.

4. **`recent_count` Missing in `-i` flag:** If this isn't provided then we just don't display the stats table instead we display the message that since no number of most recent was provided the table wasn't displayed.

5. **Path in -T flag is missing:** If the path is missing we give the error that no path was provided  and exit the program. 

## Tradeoffs considered (option A vs B, why chosen)

## Test plan (how I will know it works)

---

## Specific Design Questions

#### (a) What does the fetch layer return now, since fetch_json returns only JSON but this tool needs headers?

#### (b) What stops the pagination loop and what caps the repo count?

#### (c) Rate-limit policy and what the user sees

#### (d) Cache key, what is stored (body, ETag, time), and where the file lives with the path anchored to the file

#### (e) Error-to-message table

#### (f) Where the token is read and what happens if it is missing

#### (g) Call cost for a user with N repos

#### (h) Table and summary JSON layout
- **`public repo table`:** It is the table that lists all the repos of a user. The format is like:
    |S.No.|Name|Stars|Last Pushed|Forked?|
    |---|---|---|---|---|
    |1.|...|...|...|Yes|
    |2.|...|...|...|No|

    In caching, we directly save the received response but with tine like:
		```json
		{
				"time": <ISO>,
				"response": <response_received>
		}
		```	

- **`stats tables`:** It is the table that lists the `recent_count` most recent repos pushed. The format is like:
    |S.No.|Full Name|Language|Stars|Untouched|
    |---|---|---|---|---|
    ||1.|...|...|...|Yes|
    |2.|...|...|...|No|

    In caching, the JSON schema is like:
    ```json
    {
					"tine": <ISO>
        "stats":{
            "<full_name>": {
                "language": ...,
                "stars": ...,
                "untouched": ...
            },
            ...
        }
    }
    ```

- **"lang stat table":** It is the table that list the languages used in the "stats table" with number of repos using that language. The format is:
    |S.No.|Language|Number of repo used in|
    |---|---|---|
    ||1.|...|...|
    |2.|...|...|

    In caching, the JSON schema is like:
    ```json
    {
        "time": <ISO>
        "stats": {
            "language": <Numbe rof times used in stats table>,
            ...
        }
    }
    ```

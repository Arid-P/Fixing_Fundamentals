# Design: GitHub Activity Report (gh_report)

## Purpose (2 sentences)
A CLI tool to view a user's public repos, and the report of the most recently pushed repos 

## Inputs / Outputs
1. We will use `argprase` library to initially process the arguments provided when running the script, `python gh_report.py <args>` in CLI. But if no argument is provided or some are missing or invalid then we prompt the user for it as told in [1 of Failure Modes and Handling](#failure-modes-and-handling).

2. The user has main 3 tasks he can choose: `information` with flag `-i` or `-I` or `--info`, `GitHub Token` with flag `-t` or `-T` or `--token`, and `exit`, this will only be available when the user runs the scripts with no arguments, more details in [2 of Failure Modes and Handling](#failure-modes-and-handling).

3. For `information` task, the user needs to provide two inputs: `user` and `N`. `user` is for which user's repo do we have to display in the `public repo table`. `recent_count` is the number most recent repos that the script needs to process for the `stats table`. [3 and 4 of Failure](#failure-modes-and-handling), [Tables](#h-table-and-summary-json-layout)




## States and transitions (diagram or table)

## Modules and interfaces (who calls whom, with what data)

## Constraints (time, memory, hardware, cost)

## Failure modes and handling
1. **No arguments in CLI:** Then we have a proper input function that inputs which option does the user want (`information`, `GitHub Token`, `exit`).

2. **`exit` Task Option:** When we prompt the user for input, like above, we will also provide an exit option since the user has run the script without any arguments so it may be a mistake. 

3. **`user` Missing in `-i` flag:** If not provided we exit with message telling that no username was provided.

4. **`recent_count` Missing in `-i` flag:** If this isn't provided then we just don't display the stats table instead we display the message that since no number of most recent was provided the table wasn't displayed.

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

    In caching, we directly save the received response.

- **`stats tables`:** It is the table that lists the `recent_count` most recent repos pushed. The format is like:
    |S.No.|Full Name|Language|Stars|Untouched|
    |---|---|---|---|---|
    ||1.|...|...|...|Yes|
    |2.|...|...|...|No|

    In caching, the JSON schema is like:
    {
        "<full_name>": {
            "language": ...,
            "stars": ...,
            "untouched": ...
        },
        ...
    }


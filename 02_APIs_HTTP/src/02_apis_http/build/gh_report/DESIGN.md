# Design: GitHub Activity Report (gh_report)

## Purpose (2 sentences)
A CLI tool to view a user's public repos, and the report of the most recently pushed repos 

## Inputs / Outputs
1. When the software starts the user is asked if he wants the `info table` or wants to enter the `GitHub Token` or `exit`.  

2. If the user chooses the `info table`, then we enter the `userId` for which user it wants the first table regarding the public repo of a user to be. And `num_recent`, the number of most recently pushed repos whose language breakdown is required, along with the total stars, top language, whether untouched for more than 90 days.

3. If the user chooses ` GITHUB_TOKEN` then we prompt the user to create a `.env` file and save it. This option will only be shown if the Key isn't available.

4. If the user chooses `exit` we simply end the program using `exit()` function.

## States and transitions (diagram or table)

## Modules and interfaces (who calls whom, with what data)

## Constraints (time, memory, hardware, cost)

## Failure modes and handling

## Tradeoffs considered (option A vs B, why chosen)

## Test plan (how I will know it works)

---

## Specific Design Questions

### (a) What does the fetch layer return now, since fetch_json returns only JSON but this tool needs headers?

### (b) What stops the pagination loop and what caps the repo count?

### (c) Rate-limit policy and what the user sees

### (d) Cache key, what is stored (body, ETag, time), and where the file lives with the path anchored to the file

### (e) Error-to-message table

### (f) Where the token is read and what happens if it is missing

### (g) Call cost for a user with N repos

### (h) Table and summary JSON layout

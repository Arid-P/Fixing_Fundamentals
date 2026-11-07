# Design: GitHub Activity Report (gh_report)

## Purpose (2 sentences)

## Inputs / Outputs

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

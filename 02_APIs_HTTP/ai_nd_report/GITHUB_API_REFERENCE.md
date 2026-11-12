# GitHub REST API Reference — `gh_report`

This reference documents the exact endpoints, headers, status codes, and schemas used by the `gh_report` CLI tool.

---

## 1. Endpoints

### 1.1 List User Repositories
* **Method & URL:** `GET https://api.github.com/users/{username}/repos`
* **Purpose:** List public repositories owned by the user.
* **Query Parameters:**
  - `per_page` (int, default `30`, max `100`): Results per page.
  - `page` (int, default `1`): Page number to fetch (1-based index).
  - `sort` (str, default `full_name`): `created`, `updated`, `pushed`, `full_name`.
  - `direction` (str, default `asc`): `asc` or `desc`.
* **Important Response Fields per Repo Object (JSON array):**
  - `name` (str): Repository name.
  - `full_name` (str): Owner and repo name (`"octocat/Hello-World"`).
  - `owner` -> `login` (str): Username of the owner.
  - `stargazers_count` (int): Number of stars.
  - `pushed_at` (str, ISO 8601): e.g. `"2026-10-15T12:00:00Z"`.
  - `fork` (bool): True if the repo is a fork.

---

### 1.2 List Repository Languages
* **Method & URL:** `GET https://api.github.com/repos/{owner}/{repo}/languages`
* **Purpose:** Breakdown of languages used in a repository by byte count.
* **Query Parameters:** None.
* **Response Body (JSON object):**
  - Key: Language name (`str`).
  - Value: Bytes of code written in that language (`int`).
  ```json
  {
    "Python": 24150,
    "Shell": 1200,
    "Makefile": 340
  }
  ```
  *(Note: If a repo is empty, GitHub returns an empty object `{}` with `200 OK`)*.

---

### 1.3 Rate Limit Status
* **Method & URL:** `GET https://api.github.com/rate_limit`
* **Purpose:** Inspect current rate limits without consuming standard core quota.
* **Response Structure:** Contains `resources.core` with `limit`, `remaining`, and `reset` (Unix epoch seconds).

---

## 2. Headers

### 2.1 Standard Request Headers Sent by Client
* `Accept: application/vnd.github+json` — Recommended GitHub media type.
* `User-Agent: <app-name>` — **Required** by GitHub (requests without User-Agent return 403).
* `Authorization: Bearer <token>` — Optional Personal Access Token (PAT).
* `If-None-Match: <etag>` — Used for conditional caching revalidation.

### 2.2 Response Headers Returned by GitHub
* `Link`: Present when response results span multiple pages.
  - Format: `<url>; rel="next", <url>; rel="last"`
  - When on the final page, `rel="next"` is omitted.
  - When results fit in 1 page, the `Link` header is absent entirely.
* `ETag`: Identifier for the exact version of the resource representation, e.g. `W/"644b5b01a0a8..."` or `"644b5b01a0a8..."`.
* `X-RateLimit-Limit`: Maximum requests per hour (60 unauthenticated, 5,000 authenticated).
* `X-RateLimit-Remaining`: Requests left in the current 1-hour window.
* `X-RateLimit-Reset`: Unix epoch timestamp (integer seconds) when the budget resets to full.
* `Retry-After`: Returned on secondary / abuse rate limits (in integer seconds).

---

## 3. Status Codes & Error Behaviors

| Status Code | Meaning in GitHub API | Typical Cause in `gh_report` |
|---|---|---|
| **200 OK** | Success | Valid data returned in response body. |
| **304 Not Modified** | Resource has not changed | Sent when `If-None-Match` matches current `ETag`. Body is completely empty. Rate limit cost is **0**. |
| **401 Unauthorized** | Bad Credentials | `GITHUB_TOKEN` is invalid, malformed, or revoked. |
| **403 Forbidden** | Rate Limit or Forbidden | Primary rate limit reached (`X-RateLimit-Remaining: 0`), or missing `User-Agent`. |
| **404 Not Found** | Resource Not Found | Username does not exist, or repo does not exist / is private. |
| **429 Too Many Requests** | Secondary Rate Limit | Triggered by rapid bursting of concurrent requests. Look for `Retry-After`. |

---

## 4. Official Documentation References

- Repos API: https://docs.github.com/en/rest/repos/repos#list-repositories-for-a-user
- Languages API: https://docs.github.com/en/rest/repos/repos#list-repository-languages
- REST Pagination: https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api
- Rate Limits: https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
- Conditional Requests: https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api#use-conditional-requests-if-appropriate

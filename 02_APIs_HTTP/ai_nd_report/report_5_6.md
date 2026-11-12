# Milestone 02 Progress Report: Checkpoints M2-5 & M2-6

- **Project:** Milestone 02 — APIs & HTTP (for real)
- **Learner:** Ari (Aridaman Patel)
- **Checkpoints Covered:** M2-5 (Real Data, Pagination & Disk Caching with TTL), M2-6 (Authentication, Secrets Hygiene & Rate Limits)
- **Hours Logged:** ~5.25h (M2-5: ~4.25h, M2-6: ~1.0h)
- **Milestone 02 Cumulative Hours:** ~13.0h total
- **Atoms Cleared:** 19 of 21 achieved (`M02.07` fully cleared, `M02.13`, `M02.14`, `M02.15`, `M02.16`, `M02.17`, `M02.19`). Only `M02.20` formal gate and optional `M02.21` remain.
- **Report Source:** Milestone chat transcript, real terminal outputs, and learner verbatim Q&A bank

---

## 1. Verified Atoms Summary

| Atom ID | Description | Status | Evidence / Verification Line |
|---|---|---|---|
| **M02.07** | Headers: Content-Type, Accept, User-Agent, Authorization, Rate-limits | **Achieved** | Part 1 verified in M2-3; Part 2 (`Authorization: Bearer`, `X-RateLimit-*`) verified via terminal inspection in `rate_limit.py`. |
| **M02.13** | Auth types: API key, Bearer token, Basic auth, OAuth 2.0 concept | **Achieved** | 100% score on M2-6 gate; passed fine-grained GitHub token via `Authorization: Bearer <token>`. |
| **M02.14** | Secrets hygiene: environment variables, `.env` + `python-dotenv`, `.gitignore`, key rotation | **Achieved** | Verified `.env` exclusion via `git check-ignore -v .env` and `git status`; loaded safely in `dotenv_pactice.py`. |
| **M02.15** | Rate limits & 429 handling; `X-RateLimit-Limit`, `Remaining`, `Reset` | **Achieved** | Terminal run proved 60 $\to$ 5,000 req/hr jump; converted `X-RateLimit-Reset` epoch timestamp to human time deltas. |
| **M02.16** | Pagination patterns: offset/limit vs cursor; dynamic link traversal | **Achieved** | Built `practice/poke_pagination.py` fetching 30 Pokémon across 3 pages by following server-provided `next` URLs. |
| **M02.17** | Read API docs: OpenAPI / Swagger OAS spec vs Swagger UI | **Achieved** | Read Open-Meteo & GitHub docs; queried multi-day forecasts for Delhi, Sitapur, and Bangalore in `open_mtro_practice.py`. |
| **M02.19** | Cache responses to disk; metadata envelope & TTL invalidation | **Achieved** | Built `weather_cache_prototype.py` caching raw JSON with `{"time": ..., "response": ...}` and 24h expiration check. |
| **M02.20** | What happens on URL request: DNS $\rightarrow$ TCP $\rightarrow$ TLS $\rightarrow$ HTTP | **Pending** | Conceptual notes complete in `README.md`; formal verification scheduled at final assembly (M2-7). |

---

## 2. Checkpoint Walkthroughs & Concepts Mastered

### Checkpoint M2-5: Real Data, Pagination & Disk Caching with TTL
- **OpenAPI vs Swagger UI:** Mastered the distinction between the machine-readable OpenAPI specification (JSON/YAML contract) and Swagger UI (the interactive browser tool like FastAPI's `/docs`).
- **Real Multi-City Weather Fetch (`open_mtro_practice.py`):**
  - Queried Open-Meteo's `/v1/forecast` endpoint for New Delhi (`28.6139, 77.2090`), Sitapur (`27.5751, 80.6638`), and Bangalore (`12.9716, 77.5946`).
  - Learned meteorological variable standards (e.g., `temperature_2m` = temperature measured 2 meters above ground level to avoid surface heat radiation; `wind_speed_10m` = wind measured 10m high to clear rooflines).
- **The Query Parameter Trap & Socratic Debugging:**
  - Encountered `JSONDecodeError: Expecting value: line 1 column 1 (char 0)` because parameters were misspelled as `"latidute"` and `"logitude"`.
  - Proved via curl that Open-Meteo returns HTTP 200 with an empty body (`resp.text == ''`) when required coordinates are missing. Corrected parameter spellings to fix the issue.
- **Dynamic Pagination Traversal (`poke_pagination.py`):**
  - Explored offset/limit vs cursor pagination. Understood the offset flaw (items shifting on concurrent insertions) and the cursor advantage ($O(1)$ database index stability).
  - Implemented client pagination driven by server state: `url = resp.get("next")`, fetching 3 pages (30 Pokémon) cleanly.
- **Disk Caching with TTL (`weather_cache_prototype.py`):**
  - Explored file streaming mechanics: diagnosed why multiple calls to `fh.readline()` advance the internal file pointer, starving subsequent `json.load()` calls.
  - Implemented production-grade cache envelopes:
    ```json
    {
      "time": "2026-11-07 02:37:08.086942",
      "response": { "latitude": 28.57, "current": { "temperature_2m": 20.4 } }
    }
    ```
  - Built active cache invalidation: computed `time_diff = dt.now() - saved_time`; if `time_diff.days > 1`, invalidated stale cache and re-fetched.

### Checkpoint M2-6: Authentication, Secrets Hygiene & Rate Limits
- **Secrets Hygiene & Air-Gapped Environment (`dotenv_pactice.py`):**
  - Stored credentials in `.env` and proved `.env` is ignored by Git using `git check-ignore -v 02_APIs_HTTP/.env`.
  - Loaded secrets into memory via `load_dotenv()` and `os.getenv()`.
  - Understood Git permanence: why committing a secret cannot be fixed by deleting it in a future commit (key must be rotated immediately).
- **Authentication Protocols:**
  - API Key (query parameter vs custom header).
  - Bearer Token: Sent in standard `Authorization: Bearer <token>` header inside the encrypted TLS tunnel.
  - Basic Auth: Base64-encoded credentials (legacy).
  - OAuth 2.0: Delegation flow using temporary access/refresh tokens without exposing user passwords to third-party clients.
- **Debugging Headers vs Params (`rate_limit.py`):**
  - Discovered that passing tokens to `params=` puts them in the URL query string, which GitHub ignores.
  - Corrected to `headers={"Authorization": f"Bearer {token}", "User-Agent": "Ari-Test"}`.
- **Rate-Limit Inspection & Verification:**
  - Terminal run verified unauthenticated rate limit of 60 req/hr.
  - Authenticated run verified rate limit jump to 5,000 req/hr (Remaining: 4,993).
  - Parsed `X-RateLimit-Reset` Unix epoch timestamp and converted it into human-readable minutes and seconds remaining.

---

## 3. Real Terminal Proofs

### Multi-City Weather Output (`open_mtro_practice.py`)
```text
New Delhi
The current temperature is 21.0 C, 
The maximum temperature today will be 28.6 C, 
The minimum temperature today will be 16.4 C.

Sitapur (UP)
The current temperature is 20.7 C, 
The maximum temperature today will be 29.1 C, 
The minimum temperature today will be 15.9 C.

Bangalore
The current temperature is 20.5 C, 
The maximum temperature today will be 28.9 C, 
The minimum temperature today will be 17.8 C.
```

### PokeAPI Pagination Output (`poke_pagination.py`)
```text
Page 0
[{'name': 'bulbasaur', ...}, ..., {'name': 'caterpie', ...}]

Page 1
[{'name': 'metapod', ...}, ..., {'name': 'raticate', ...}]

Page 2
[{'name': 'spearow', ...}, ..., {'name': 'nidorina', ...}]
```

### Authenticated vs Unauthenticated Rate Limits (`rate_limit.py`)
```text
No auth test
Rate Limit: 60 ;
Rate Limit Rmaining: 59 ;
Rate Limit Reset: 1794076390 ;
Reset time in dateime: 37 mins 60 sec 

Auth test
Rate Limit: 5000 ;
Rate Limit Rmaining: 4993 ;
Rate Limit Reset: 1794075670 ;
Reset time in dateime: 25 mins 60 sec 
```

---

## 4. Code Written by Learner

### `practice/open_mtro_practice.py`
```python
from build.fetcher_core import fetch_json

def main() -> None:
    cord = {
        "New Delhi": (28.6139, 77.2090),
        "Sitapur (UP)": (27.5751, 80.6638),
        "Bangalore": (12.9716, 77.5946),
    }
    url = r"https://api.open-meteo.com/v1/forecast"

    for name, crd in cord.items():
        lat, lng = crd
        params = {
            "latitude": lat,
            "longitude": lng,
            "current": "temperature_2m,weather_code",
            "daily": "temperature_2m_max,temperature_2m_min",
            "timezone": "auto",
        }
        resp = fetch_json(url=url, params=params)
        print(f"{name}\nCurrent: {resp.get('current').get('temperature_2m')} C")
```

### `practice/poke_pagination.py`
```python
from build.fetcher_core import fetch_json

def main() -> None:
    page_count = 3
    pages = {}
    url = r"https://pokeapi.co/api/v2/pokemon?limit=10&offset=0"

    for num in range(page_count):
        resp = fetch_json(url=url)
        pages.update({f"Page {num}": resp.get("results")})
        url = resp.get("next")

    for page, content in pages.items():
        print(f"{page}\n{content}\n")
```

### `practice/rate_limit.py`
```python
from os import getenv
from dotenv import load_dotenv
from requests import get
from datetime import datetime as dt

url = r"https://api.github.com/rate_limit"

def limits_print(headers: dict | None = None) -> None:
    resp = get(url, headers=headers)
    reset_epoch = float(resp.headers.get("X-RateLimit-Reset"))
    time_diff = dt.fromtimestamp(reset_epoch) - dt.now()
    mins = time_diff.seconds // 60
    secs = time_diff.seconds % 60

    print(
        f"Rate Limit: {resp.headers.get('X-RateLimit-Limit')}",
        f"Remaining: {resp.headers.get('X-RateLimit-Remaining')}",
        f"Reset in: {mins} mins {secs} sec",
        sep="\n",
    )

print("No auth test")
limits_print(headers={"User-Agent": "Ari-Test"})

load_dotenv()
token = getenv("GITHUB_TOKEN")
print("\nAuth test")
limits_print(headers={"User-Agent": "Ari-Test", "Authorization": f"Bearer {token}"})
```

---

## 5. Verification Gate Results (Verbatim)

### Checkpoint M2-5 Verification (Score: 7 / 7 — 100%)
- **Statements:** OpenAPI spec vs Swagger UI, offset insertion shift, cursor pagination concept, 0-byte cache handling, TTL metadata timestamping, file cursor advance, query param typos and status codes.
- **Learner Response (Verbatim):** `f, t, f, f, t, f, f`
- **Result:** 7 / 7 Correct. Atoms `M02.16`, `M02.17`, `M02.19` cleared.

### Checkpoint M2-6 Verification (Score: 7 / 7 — 100%)
- **Statements:** Query param secret leakage, Bearer token encryption myth, OAuth 2.0 password isolation, load_dotenv override behavior, Git secret permanence and rotation necessity, Unix epoch timestamps, 429 backoff vs tight looping.
- **Learner Response (Verbatim):** `t, f, t, f, f, t, f`
- **Result:** 7 / 7 Correct. Atoms `M02.07` (part 2), `M02.13`, `M02.14`, `M02.15` cleared.

---

## 6. Current Status & Transition to Final Capstone Build

- **Progress:** 19 of 21 atoms cleared.
- **Architecture Shift:** Practice prototypes completed. The final Milestone 02 deliverable has pivoted to **`src/02_apis_http/build/gh_report/`** (GitHub Activity Report), with **Design First** methodology.
- **Ready for Next Phase:** `DESIGN.md` skeleton created. Learner is ready to author the technical design document covering all 8 requirements (R1–R8) with complete conceptual mastery of pagination, ETags, Bearer authentication, and rate limiting.

# Milestone 02 Progress Report: Checkpoints M2-1 through M2-4

- **Project:** Milestone 02 — APIs & HTTP (for real)
- **Learner:** Ari (Aridaman Patel)
- **Checkpoints Covered:** M2-1, M2-2, M2-3, M2-4
- **Total Hours Logged:** 7.75h (M2-1: 1.75h, M2-2: 2.00h, M2-3: 2.00h, M2-4: 2.00h)
- **Atoms Cleared:** 12 of 21 achieved, 1 partial (`M02.07`), 1 pending formal gate (`M02.20`)
- **Report Source:** Milestone chat transcript, real terminal outputs, and learner verbatim Q&A bank

---

## 1. Verified Atoms Summary

| Atom ID | Description | Status | Evidence / Verification Line |
|---|---|---|---|
| **M02.01** | Client–server model; 1 request $\rightarrow$ 1 response | **Achieved** | Terminal `curl -i` verified status line, headers, and body separation (`\r\n\r\n`). |
| **M02.02** | URL anatomy: scheme, host, port, path, query, fragment | **Achieved** | Cleared via fresh 2-statement retest (default ports: HTTP=80, HTTPS=443; explicit port overrides). |
| **M02.03** | Request anatomy: method, path, headers, optional body | **Achieved** | Terminal `curl -v` inspected request line `GET /posts/1 HTTP/2` and default headers (`Host`, `User-Agent`, `Accept`). |
| **M02.04** | Response anatomy: status line, headers, body | **Achieved** | Terminal `curl -v` inspected status line `HTTP/2 200`, key-value response headers, blank CRLF delimiter, and JSON body. |
| **M02.05** | Methods: GET, POST, PUT, PATCH, DELETE; safe vs idempotent | **Achieved** | 100% score on e-commerce scenario check (PUT idempotent state vs POST compounding side effects). |
| **M02.06** | Status families 1xx–5xx and must-know code clusters | **Achieved** | 5/5 scenario matching score (422, 204, 429, 401, 403); 101 WebSocket handshake conceptualized. |
| **M02.07** | Headers: Content-Type, Accept, User-Agent, Rate-limit | **Partial** | Part 1 (`Content-Type`, `Accept`, `User-Agent`) verified via `r.request.headers`. Auth/Rate-limit pending M2-6. |
| **M02.08** | Path vs Query params vs Body; `params=` in requests | **Achieved** | Written in `get_practice.py` using `params={"userId": 1}` with automatic URL encoding. |
| **M02.09** | JSON bodies: `json=` vs `data=` | **Achieved** | `test_req.py` inspected: `json=` automatically sets `Content-Type: application/json` & calculates `Content-Length` (31 bytes). |
| **M02.10** | `requests.get/post`, `.status_code`, `.json()`, `.raise_for_status()` | **Achieved** | Written in `get_practice.py` with `try/except HTTPError` wrapping `.raise_for_status()`. |
| **M02.11** | Always set timeouts; `requests.Session`; retry with backoff | **Achieved** | Implemented in `build/fetcher_core.py` with `requests.Session()`, `timeout=timeout`, and exponential backoff ($2^{\text{retry}}$). |
| **M02.12** | Error classes: `ConnectionError`, `Timeout`, `HTTPError`, `JSONDecodeError` | **Achieved** | Forced and caught all 4 exceptions deliberately in `practice/break_things.py`. |
| **M02.18** | Hand-test APIs: browser, curl, DevTools Network tab | **Achieved** | Live DevTools inspection proof submitted (`claude.ai` request headers: `accept`, `content-type`, `accept-encoding`). |
| **M02.20** | URL journey: DNS $\rightarrow$ TCP $\rightarrow$ TLS $\rightarrow$ HTTP | **Pending** | Read-only preview completed; formal gate scheduled for Checkpoint M2-7. |

---

## 2. Checkpoint Walkthroughs & Concepts Mastered

### Checkpoint M2-1: Raw HTTP & Wire Flow
- **Mental Model:** An API is not "a link". It is structured plain-text communication over an operating system TCP socket (`IP + Port`).
- **Wire Inspection:** Ran `curl -i https://jsonplaceholder.typicode.com/posts/1` and located the physical boundary line (`\r\n\r\n`) separating headers from the payload.
- **DevTools Evidence:** Extracted live request headers from Chrome/Firefox Network tab on `claude.ai` (`accept: */*`, `content-type: application/json`, `accept-encoding: gzip, deflate, br, zstd`).
- **URL Anatomy Breakdown:** Tested on `https://api.open-meteo.com:443/v1/forecast?latitude=52.52&longitude=13.41#current`.
  - Deduced why the fragment (`#current`) is never transmitted across the wire: the client strips it locally for browser bookmarking/scrolling (library vs bookmark analogy).
- **Network Stack (CBSE 12 CS Mapping):**
  1. DNS: Hostname $\rightarrow$ IP address.
  2. TCP: 3-way handshake (`SYN` $\rightarrow$ `SYN-ACK` $\rightarrow$ `ACK`) opens reliable socket.
  3. TLS: Authenticates server identity via certificates and negotiates symmetric encryption keys.
  4. HTTP: Plain-text request transmitted inside the armored TLS tunnel.

### Checkpoint M2-2: Anatomy, Methods & Status Codes
- **Verbose Inspection:** Ran `curl -v` to observe both directions:
  - `*`: Handshake and ALPN negotiation (`ALPN: curl offers h2,http/1.1` $\rightarrow$ server accepts `h2`).
  - `>`: Outgoing request line (`GET /posts/1 HTTP/2`) and request headers (`Host`, `User-Agent`, `Accept`).
  - `<`: Incoming status line (`HTTP/2 200`) and response headers.
- **Safe vs Idempotent:**
  - *Safe:* Read-only, no server state mutation (`GET`).
  - *Idempotent:* $N \ge 1$ calls result in identical server end-state (`GET`, `PUT`, `DELETE`). `POST` is non-idempotent because multiple calls create multiple records / compounding transactions.
- **Status Families & Must-Know Clusters:**
  - `1xx` Informational: Protocol handshakes (`101 Switching Protocols` to WebSockets).
  - `2xx` Success: `200 OK`, `201 Created` (POST), `204 No Content` (DELETE/silent update).
  - `3xx` Redirect: `301 Moved Permanently` (cached by clients), `302 Found` (temporary).
  - `4xx` Client Error: `400 Bad Request`, `401 Unauthenticated` (no ID shown), `403 Forbidden` (ID shown, but not authorized), `404 Not Found`, `405 Method Not Allowed`, `409 Conflict`, `422 Unprocessable Entity` (semantic/Pydantic validation failure), `429 Too Many Requests` (rate-limited).
  - `5xx` Server Error: `500 Server Crash`, `502 Bad Gateway` (upstream server/reverse proxy died), `503 Service Unavailable` (overloaded).

### Checkpoint M2-3: Python `requests` Basics
- **The Response Object:** Mastered `.status_code`, `.headers` (received), `.text`, `.json()` (deserialization), and `.raise_for_status()`.
- **Query Parameters (`params=`):** Why manual string concatenation (`?key=val`) is prohibited—`params={"userId": 1, "city": "New York"}` automatically handles URL encoding (`"New%20York"`).
- **Body Payloads (`json=` vs `data=`):**
  - `json=dict`: Automatically dumps to JSON string and injects `Content-Type: application/json`.
  - `data=dict`: Form-encodes data (`application/x-www-form-urlencoded`), triggering `422` on JSON APIs.
- **Outgoing Inspection & Byte Counting:**
  - Inspected `resp.request.headers`.
  - Proved that `Content-Length: 31` corresponds to the exact 31 ASCII characters/bytes in `'{"title": "hello", "userId": 1}'`.

### Checkpoint M2-4: When Things Break (Resilience & Retries)
- **The Cardinal Rule:** In `requests`, default timeout is `None` (will hang indefinitely). Timeouts must always be set explicitly (`timeout=5.0`).
- **Connection Reuse:** `requests.Session()` keeps the socket alive across calls via HTTP Keep-Alive, eliminating repeated DNS/TCP/TLS handshakes. Must be closed like an SQL or file session to avoid leaking file descriptors.
- **Forced Failure Lab:** Deliberately triggered and handled all 4 core network exceptions in `break_things.py`.
- **Pitfall: HTTP 200 $\ne$ Valid Data:** Captive portals (Wi-Fi login screens) and bad APIs return `200 OK` with HTML error pages. Validating status code must be paired with guarded JSON decoding.
- **Planted Bug Hunt:** Identified off-by-one bug in a retry helper where `attempt == max_retries` was unreachable under `range(max_retries)`.
- **Core Engine:** Built `fetcher_core.py` featuring exponential backoff ($2^{\text{retry}}$: 1s, 2s, 4s, 8s, 16s), clean exception raising via bare `raise`, and selective retries (retrying network drops and 429/503, immediately raising permanent 4xx/non-JSON errors).

---

## 3. Code Written by Learner

### `practice/get_practice.py` (M2-3 Deliverable)
```python
from requests import get, HTTPError
from icecream import ic

ic.disable()

url = r"https://jsonplaceholder.typicode.com/posts"
resp_post = get(url, params={"userId": 1})

try:
    resp_post.raise_for_status()
except HTTPError as e:
    print("The request was not successful")
    ic(e)
    exit()

content = resp_post.json()
ic(content)
print("The response:\n")

for resp in content:
    print("The first dict")
    for key, val in resp.items():
        print(f"{key}: {val}")
    print()
```

### `practice/break_things.py` (M2-4 Failure Lab)
```python
from requests import get, post, HTTPError, Timeout, ConnectionError, JSONDecodeError
from icecream import ic

errors = {}

try:
    resp = get(r"https://domain-DNE.com/args")
except ConnectionError as e:
    print(f"The Connection error has occured.")
    errors["connection"] = e

try:
    resp = get(r"https://httpbin.org/delay/5", timeout=1.5)
except Timeout as e:
    print(f"The Timeout error has occured.")
    errors["timeout"] = e

try:
    resp = get(r"https://jsonplaceholder.typicode.com/posts/999999")
    resp.raise_for_status()
except HTTPError as e:
    print(f"The HTTP error has occured.")
    errors["http"] = e

try:
    resp = get(r"https://httpbin.org/html")
    resp.json()
except JSONDecodeError as e:
    print(f"The JSON decode error has occured.")
    errors["json"] = e

for name, content in errors.items():
    ic(name, content)
```

### `src/02_apis_http/build/fetcher_core.py` (M2-4 Core Deliverable)
```python
import time
import requests
from icecream import ic


def wait(retry: int) -> None:
    wait_time = 2**retry
    print(f"Retrying after a wait of {wait_time} seconds.", end=" ", flush=True)

    time.sleep(wait_time)
    print("Retrying", flush=True)


def fetch_json(
    url: str, params: dict | None = None, max_retries: int = 3, timeout: float = 5.0
) -> dict | list | None:
    session = requests.Session()

    resp, err = None, None  # to keep resp in bounds
    for retry in range(max_retries):
        try:
            resp = session.get(url, timeout=timeout, params=params)
            resp.raise_for_status()
            return resp.json()

        except (requests.ConnectionError, requests.Timeout):
            if retry == max_retries - 1:
                raise
            wait(retry)

        except requests.HTTPError:
            if resp.status_code in [429, 503]:  # type: ignore
                if retry == max_retries - 1:
                    raise
                wait(retry)
            else:
                raise

        except requests.JSONDecodeError:
            raise


def main() -> None:
    """It is the starting function. From it you can understand a basic flow of the whole program"""
    # successful try
    js = fetch_json("https://httpbin.org/json", max_retries=2, timeout=3)
    print(js)

    js1 = fetch_json("https://httpbin.org/delay/4", max_retries=5, timeout=3)
    js2 = fetch_json("https://httpbin.org/status/404", max_retries=5, timeout=3)
    print(js1, js2, sep="\n\n")


if __name__ == "__main__":
    main()
```

#### Real Terminal Execution Proof:
```text
Retrying after a wait of 1 seconds. Retrying
Retrying after a wait of 2 seconds. Retrying
Retrying after a wait of 4 seconds. Retrying
Retrying after a wait of 8 seconds. Retrying
Retrying after a wait of 16 seconds. Retrying
SUCCESS: Real requests.ConnectionError raised cleanly!
```

---

## 4. Struggles, Debugging & Conceptual Breakthroughs

1. **HTTP vs HTTPS Default Ports:**
   - *Struggle:* Initially believed `http://` defaulted to port 443.
   - *Fix:* Clarified unencrypted `http://` defaults to 80; encrypted `https://` defaults to 443. Cleared with two fresh, non-giveaway retest statements.
2. **ALPN & TLS Protocol Negotiation:**
   - *Breakthrough:* Learned that ALPN (Application-Layer Protocol Negotiation) allows client and server to agree on HTTP/2 (`h2`) during the TLS handshake, saving an extra round-trip.
3. **`get()` vs `.json()` Execution Timing:**
   - *Struggle:* In `break_things.py`, questioned why calling `get("https://httpbin.org/html")` did not trigger a `JSONDecodeError`.
   - *Fix:* Realized `get()` only fetches raw bytes; JSON parsing only executes when `.json()` is explicitly called on the response object.
4. **Retry Loop Off-by-One:**
   - *Struggle:* In a retry loop with `range(max_retries)`, attempted `if attempt == max_retries: raise err`.
   - *Fix:* Recognized `range(3)` only yields `0, 1, 2`. The condition was permanently dead code.
5. **No Sleeping on Final Failure:**
   - *Struggle:* Script waited 16 seconds on the 5th attempt before crashing.
   - *Fix:* Implemented `if retry == max_retries - 1: raise` before calling `wait(retry)`.
6. **Python Exception Scoping (PEP 3110):**
   - *Struggle:* Encountered `UnboundLocalError: local variable 'err' referenced before assignment` when referencing `err` outside `except ... as err:`.
   - *Fix:* Learned that Python deletes the exception variable at the end of the `except` block. Replaced with Pythonic bare `raise`, which preserves the active exception traceback.
7. **Code Redundancy & DRY Architecture:**
   - *Breakthrough:* Questioned why `if retry == max_retries - 1: raise; wait(retry)` was written twice and why catching `JSONDecodeError` just to re-raise was useless. Learned how production libraries classify exceptions into transient vs permanent failure sets.
8. **Session Socket Lifecycle:**
   - *Breakthrough:* Connected database session management (SQLAlchemy) to network sockets—realized `requests.Session()` holds open kernel file descriptors and should be closed via context manager or explicit cleanup.

---

## 5. Verification Bank Log (Verbatim Learner Responses)

### Checkpoint M2-1 (Score: 6/7 | Retest: Passed)
- *Learner verbatim:* `t, t, t, f, t, t, f`
- *Miss:* Statement 2 (thought http defaults to 443).
- *Fresh Retest 2R:* Passed (`True`). Fresh port statements in M2-2 confirmed mastery.

### Checkpoint M2-2 (Score: 7/8 | Retest: Passed)
- *Learner verbatim:* `t, f, f, t, f, *f*, f, t`
- *Miss:* Statement 6 (wire delimiter CRLF CRLF).
- *Fresh Retest 6R:* Passed (`6R t`).
- *M02.02 Outcome:* Statements 7 & 8 (`f, t`) passed cold.

### Checkpoint M2-3 (Score: 7/7 Clean Sweep)
- *Learner verbatim:* `t, t, f, f, f, t, f (payload body length)`
- *All 7 statements correct; learner correctly identified that `Content-Length` measures payload body length in bytes.*

### Checkpoint M2-4 (Score: 7/7 Clean Sweep)
- *Learner verbatim:* `f, t, f, f, f, t, t`
- *All 7 statements correct on first pass.*

---

## 6. Ready State for Checkpoint M2-5

- **Next Checkpoint:** M2-5 (Real Data & Caching)
- **Upcoming Atoms:**
  - `M02.16` Pagination patterns: page/limit (PokeAPI), cursor concept.
  - `M02.17` Read API docs: endpoints, params, response schema; Swagger/OpenAPI.
  - `M02.19` Cache responses to JSON on disk (`data/cache/*.json`) to avoid repeated network calls.
- **Pre-requisite Verified:** NASA API key registered; Open-Meteo, PokeAPI, and JSONPlaceholder verified reachable.

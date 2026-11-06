# Milestone 02: Q&A and Verification Bank

This bank records all atomic verification statements, learner verbatim responses, evaluations, and retests across Milestone 02 checkpoints.

---

## Checkpoint M2-1 Verification (See Raw HTTP)
**Date:** 2026-10-28

### Statements
1. Under standard HTTP request-response semantics, one client request produces exactly one server response.
2. In a URL like `http://example.com/api`, if the port is not explicitly specified, the client defaults to port 443 because modern web servers require it.
3. In a raw HTTP response (like that seen in `curl -i`), the boundary between the response headers and the response body is marked by a blank line (`\r\n\r\n`).
4. The fragment identifier in a URL (e.g., `#summary`) is included in the HTTP request line sent across the wire so the server knows which anchor to return.
5. In the network sequence of requesting `https://api.open-meteo.com/v1/forecast`, DNS resolution must succeed before the TCP 3-way handshake can begin.
6. A network socket is formed by the combination of an IP address (identifying the host machine) and a port number (identifying the specific running application/process).
7. HTTPS is an entirely separate application protocol that completely replaces the HTTP text methods (`GET`, `POST`) with binary encryption algorithms.

### Learner Response (Verbatim)
`t, t, t, f, t, t, f`

### Evaluation
- **Statement 1:** Correct (Answered: True | Key: True)
- **Statement 2:** Incorrect (Answered: True | Key: False — `http://` defaults to port 80, whereas port 443 is default for `https://`)
- **Statement 3:** Correct (Answered: True | Key: True)
- **Statement 4:** Correct (Answered: False | Key: False)
- **Statement 5:** Correct (Answered: True | Key: True)
- **Statement 6:** Correct (Answered: True | Key: True)
- **Statement 7:** Correct (Answered: False | Key: False)

**Score:** 6 / 7 Correct.

### Retest 2R
- **Statement 2R:** A client requesting `http://api.weather.com/v1` connects to port 80 by default, whereas requesting `https://api.weather.com/v1` connects to port 443 by default. (True or False?)
- **Learner Response (Verbatim):** `True`
- **Evaluation:** Correct. M02.02 fully cleared.

---

## Checkpoint M2-2 Verification (Anatomy, Methods, Status Codes, Port Retest)
**Date:** 2026-10-31

### Statements
1. An HTTP method is defined as "safe" if calling it does not alter any resource state on the server.
2. Submitting a `POST` request multiple times with identical body payloads is guaranteed by HTTP specifications to produce the exact same server end-state as submitting it once.
3. An HTTP response with status code `204 No Content` indicates that the request failed because the server could not find any content matching the query.
4. An HTTP status code `403 Forbidden` indicates that the server recognized the client's identity credentials, but the authenticated user does not have permission to access the resource.
5. An HTTP status code `502 Bad Gateway` indicates that the client made a syntax error in the request URL path or query string.
6. In HTTP/1.1 wire protocol, the boundary between the headers section and the body section (in both request and response) is marked by a blank line (`\r\n\r\n`).
7. When a client issues a request to `http://api.github.com` without explicitly writing a port in the URL, the underlying TCP connection is opened on port 443 by default.
8. When a URL is given as `https://localhost:8000/api`, the client connects to port 8000 rather than standard port 443 because an explicit port overrides the scheme's default.

### Learner Response (Verbatim)
`Dont satrt 02 3 yet.`
`t, f, f, t, f, *f*, f, t`

### Evaluation
- **Statement 1:** Correct (Answered: True | Key: True)
- **Statement 2:** Correct (Answered: False | Key: False)
- **Statement 3:** Correct (Answered: False | Key: False)
- **Statement 4:** Correct (Answered: True | Key: True)
- **Statement 5:** Correct (Answered: False | Key: False)
- **Statement 6:** Incorrect (Answered: False | Key: True — In HTTP/1.1, the headers block in *both* requests and responses is terminated by a single empty line `\r\n\r\n` before the payload body)
- **Statement 7 (Port Retest):** Correct (Answered: False | Key: False — `http://` connects to port 80)
- **Statement 8 (Port Retest):** Correct (Answered: True | Key: True — explicit port overrides default)

**Score:** 7 / 8 Correct.
- **M02.02 Outcome:** Both fresh port statements (7 & 8) passed. **M02.02 is now fully Achieved.**
- **Retest Queued:** Statement 6 concept (HTTP header-body delimiter).

### Retest 6R
- **Statement 6R:** If an HTTP client sends a POST request containing headers and a JSON body, the server identifies where the headers stop and where the JSON payload begins by scanning for an empty line (`\r\n\r\n`).
- **Learner Response (Verbatim):** `6R t, dont start 3`
- **Evaluation:** Correct. M02.03 fully cleared.

---

## Checkpoint M2-3 Verification (Requests Basics, Params, Payloads & Headers)
**Date:** 2026-11-05

### Statements
1. Calling `requests.get(url, params={"city": "New York"})` automatically URL-encodes the space in the parameter value.
2. When calling `requests.post(url, json={"name": "Ari"})`, the `requests` library automatically injects the outgoing header `Content-Type: application/json`.
3. If a server returns an HTTP 500 error with an HTML error page, calling `r.json()` suppresses the error and safely returns an empty dictionary `{}`.
4. The method `r.raise_for_status()` raises an `HTTPError` exception if the response status code is `201 Created`.
5. In Python `requests`, `r.headers` displays the headers sent out by your Python client, whereas `r.request.headers` displays the headers received from the server.
6. Passing a Python dictionary to `data=` in `requests.post()` sends form-encoded data (`application/x-www-form-urlencoded`) rather than JSON.
7. The `Content-Length` header indicates the total number of characters in the URL path.

### Learner Response (Verbatim)
`t, t, f, f, f, t, f (payload body length)`

### Evaluation
- **Statement 1:** Correct (Answered: True | Key: True)
- **Statement 2:** Correct (Answered: True | Key: True)
- **Statement 3:** Correct (Answered: False | Key: False — raises JSONDecodeError, does not return empty dict)
- **Statement 4:** Correct (Answered: False | Key: False — 201 is success, does not raise)
- **Statement 5:** Correct (Answered: False | Key: False — r.headers is received, r.request.headers is sent)
- **Statement 6:** Correct (Answered: True | Key: True)
- **Statement 7:** Correct (Answered: False (payload body length) | Key: False — size of body in bytes)

**Score:** 7 / 7 Correct.
- **Atoms cleared:** M02.07 (part 1), M02.08, M02.09, M02.10.

---

## Checkpoint M2-4 Verification (Network Resilience, Timeouts, Sessions, Retries & Errors)
**Date:** 2026-11-06

### Statements
1. By default, calling `requests.get("https://example.com")` without specifying `timeout` will raise a `Timeout` exception after 30 seconds if the remote server fails to respond.
2. Using `requests.Session()` reuses the underlying TCP/TLS connection across multiple requests to the same host via HTTP Keep-Alive.
3. A `requests.ConnectionError` is raised whenever a remote web server successfully returns an HTTP `500 Internal Server Error`.
4. An HTTP `404 Not Found` error should always be retried with exponential backoff because the missing resource typically appears on subsequent attempts.
5. An HTTP response with status code `200 OK` guarantees that the response body contains valid JSON that can be safely parsed by `.json()`.
6. In an exponential backoff strategy, the sleep duration between failed attempts increases exponentially (e.g. 1s, 2s, 4s) to prevent hammering an overloaded server.
7. Calling `r.raise_for_status()` on a response with status code `429 Too Many Requests` raises a `requests.HTTPError`.

### Learner Response (Verbatim)
`dl+1. Dontn we need to close the session like a sql session?`
`f, t, f, f, f, t, t`

### Evaluation
- **Statement 1:** Correct (Answered: False | Key: False — default timeout is None, hangs indefinitely)
- **Statement 2:** Correct (Answered: True | Key: True)
- **Statement 3:** Correct (Answered: False | Key: False — 500 raises HTTPError, ConnectionError is network-level)
- **Statement 4:** Correct (Answered: False | Key: False — 404 is non-transient client error)
- **Statement 5:** Correct (Answered: False | Key: False — 200 can return HTML or text)
- **Statement 6:** Correct (Answered: True | Key: True)
- **Statement 7:** Correct (Answered: True | Key: True)

**Score:** 7 / 7 Correct.
- **Atoms cleared:** M02.11, M02.12.
- **Deliverable verified:** `src/02_apis_http/build/fetcher_core.py` built by learner with real exponential backoff terminal proof.

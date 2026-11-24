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

---

## Checkpoint M2-5 Verification (Real Data, Pagination, Caching & File I/O)
**Date:** 2026-11-07

### Statements
1. An OpenAPI document is an interactive HTML web page with forms that developers click in a browser to test API endpoints.
2. In offset/limit pagination, if a new record is inserted into page 1 while a user is reading, requesting page 2 on the next call can shift items and cause the client to see a duplicate record.
3. In cursor-based pagination, the client passes an integer offset parameter so the server's database can scan and skip that exact number of rows.
4. When implementing disk caching, the presence of a 0-byte file on disk should be treated as a valid cache hit and parsed directly using `json.load()`.
5. A Time-To-Live (TTL) cache invalidation strategy requires storing timestamp metadata alongside the cached payload so the client can evaluate whether the data has expired.
6. Calling `fh.readline()` on an open Python file object inspects the next line of text without advancing the internal file cursor for subsequent read operations.
7. If an API endpoint requires `latitude` and `longitude` query parameters, submitting misspelled parameter names (like `latidute`) will always produce an HTTP `404 Not Found` status code.

### Learner Response (Verbatim)
`f, t, f, f, t, f, f`

### Evaluation
- **Statement 1:** Correct (Answered: False | Key: False — OpenAPI is a machine-readable JSON/YAML spec; Swagger UI is the HTML interface)
- **Statement 2:** Correct (Answered: True | Key: True — inserting rows into page 1 shifts offset boundaries)
- **Statement 3:** Correct (Answered: False | Key: False — cursor pagination sends an opaque pointer/ID, not an integer skip offset)
- **Statement 4:** Correct (Answered: False | Key: False — 0-byte file is unparseable and must be treated as a cache miss)
- **Statement 5:** Correct (Answered: True | Key: True — TTL relies on recorded timestamp metadata to calculate freshness)
- **Statement 6:** Correct (Answered: False | Key: False — fh.readline() consumes bytes and advances the file cursor forward)
- **Statement 7:** Correct (Answered: False | Key: False — route exists; missing/invalid query params yield 400/422 or empty 200, not 404)

**Score:** 7 / 7 Correct.
- **Atoms cleared:** M02.16, M02.17, M02.19.

---

## Checkpoint M2-6 Verification (Auth Types, Secrets Hygiene & Rate Limits)
**Date:** 2026-11-07

### Statements
1. Passing an API key in a URL query parameter (e.g. `?api_key=secret`) is inherently less secure than passing it in an `Authorization` header because URLs can be logged in plain text by browser history, proxy servers, and access logs.
2. The `Bearer` authentication scheme requires the client to encrypt the token using the server's public key before attaching it to the `Authorization` header.
3. In OAuth 2.0, the authorization code flow allows a user to grant a third-party application access to their data without ever exposing their actual account password to that application.
4. Calling `load_dotenv()` will override any existing environment variables that were already exported in the shell by default unless configured otherwise.
5. If an API secret is accidentally committed and pushed to a public GitHub repo, deleting the secret in a new commit and pushing again is sufficient to keep the secret secure.
6. The `X-RateLimit-Reset` header typically contains an integer representing Unix Epoch time (seconds since Jan 1, 1970 UTC) indicating when the rate limit window refreshes.
7. If an API returns status code `429 Too Many Requests`, a well-behaved client should immediately spin in a tight `while True` loop retrying the request every 10 milliseconds until it succeeds.

### Learner Response (Verbatim)
`t, f, t, f, f, t, f`

### Evaluation
- **Statement 1:** Correct (Answered: True | Key: True — URLs get recorded in server logs and browser histories; headers are suppressed)
- **Statement 2:** Correct (Answered: False | Key: False — Bearer token is transmitted as an unencrypted string within the encrypted TLS tunnel)
- **Statement 3:** Correct (Answered: True | Key: True — OAuth 2.0 delegates authentication via temporary tokens without exposing credentials)
- **Statement 4:** Correct (Answered: False | Key: False — python-dotenv defaults to `override=False`, preserving existing environment variables)
- **Statement 5:** Correct (Answered: False | Key: False — Git retains commits in history; leaked secrets must be rotated immediately)
- **Statement 6:** Correct (Answered: True | Key: True — X-RateLimit-Reset is a standard Unix epoch integer timestamp)
- **Statement 7:** Correct (Answered: False | Key: False — tight retries hammer servers and worsen rate bans; client must respect backoff or Retry-After)

**Score:** 7 / 7 Correct.
- **Atoms cleared:** M02.07 (part 2 fully cleared), M02.13, M02.14, M02.15.



---

## Checkpoint M2-7 Verification (Final Capstone & Request Lifecycle: DNS -> TCP -> TLS -> HTTP)
**Date:** 2026-11-24

### Statements
1. DNS resolution uses UDP by default to query port 53 and convert a human-readable hostname into an IP address before any TCP connection can be initiated.
2. The TCP three-way handshake (SYN -> SYN-ACK -> ACK) happens *after* the TLS handshake has already encrypted the channel.
3. In the sequence of an HTTPS request, DNS resolution occurs first to find the IP, then the TCP handshake establishes the raw connection, then TLS encrypts that connection, and only then is the HTTP request transmitted.
4. Because HTTPS encrypts the traffic, the domain/hostname (`api.github.com`) is completely hidden from your Internet Service Provider (ISP) during the initial DNS lookup.
5. Once the TLS session keys are established, the raw plaintext HTTP request line, headers, and body are transmitted inside TLS records, making them invisible to network sniffers on the wire.
6. A TCP socket is uniquely identified by the combination of four values: Source IP, Source Port, Destination IP, and Destination Port.
7. When you type `https://api.github.com/users` in a browser or Python script, the path `/users` is sent to the DNS server so it knows which server handle to return.

### Learner Response (Verbatim)
`1. T, 2. F, 3. T, 4. F, 5. T, 6. T, 7. F`

### Evaluation
- **Statement 1:** Correct (Answered: True | Key: True — DNS uses UDP port 53 by default for fast, low-overhead lookup)
- **Statement 2:** Correct (Answered: False | Key: False — TCP 3-way handshake MUST establish the transport connection before TLS can begin)
- **Statement 3:** Correct (Answered: True | Key: True — The strict order is: DNS -> TCP -> TLS -> HTTP)
- **Statement 4:** Correct (Answered: False | Key: False — Standard DNS queries are unencrypted and reveal the requested hostname directly to the ISP)
- **Statement 5:** Correct (Answered: True | Key: True — HTTP text is wrapped inside encrypted TLS records)
- **Statement 6:** Correct (Answered: True | Key: True — 4-tuple: src IP, src Port, dest IP, dest Port uniquely defines a TCP socket)
- **Statement 7:** Correct (Answered: False | Key: False — DNS only resolves the hostname; paths and query parameters are strictly HTTP-layer and never seen by DNS)

**Score:** 7 / 7 Correct (100%).
- **Atoms cleared:** M02.20 (Formal verification passed). Milestone 02 atoms: 20 of 21 cleared.

---

## Checkpoint M2-8 Verification: Security Hardening (S-Gate)
**Date:** 2026-11-24

### Statements
1. Setting file mode to `chmod 600` ensures that other standard user accounts on the same Linux operating system cannot read or write the contents of that file.
2. Setting `verbose=False` completely prevents all log messages from ever being written to `data/logs/app.log`, regardless of whether `logger.info()` or `logger.error()` is called.
3. Passing sensitive authentication tokens directly into `logger.debug()` is safe in production environments because Python's `logging` module automatically detects and masks tokens that start with `ghp_` or `Bearer`.
4. Removing an `ic()` print statement in the code prevents variables from being printed to the terminal, but `icecream` still writes the values into `app.log` by default in the background.
5. If a developer uses `.gitignore` to ignore `.env`, committing a script that calls `logger.info(f"Connecting with {token}")` will still leak the secret if log files or terminal output are shared or committed.
6. When reading a personal access token from an environment file using `python-dotenv`, the token value is injected into the program process's memory (`os.environ`), but it is not automatically broadcast over the network until attached to an HTTP header or payload.
7. Deleting a compromised GitHub personal access token from a local `.env` file automatically revokes that token on GitHub's authentication servers so it can no longer be used by third parties.

### Learner Response (Verbatim)
`t, f, f, f, t, t, f`

### Evaluation
- **Statement 1:** Correct (Answered: True | Key: True — `600` grants read/write to the owner only; group and others have zero permissions `---`)
- **Statement 2:** Correct (Answered: False | Key: False — `verbose=False` sets log level to `INFO`, so `INFO`, `WARNING`, `ERROR`, `CRITICAL` still get logged; only `DEBUG` is omitted)
- **Statement 3:** Correct (Answered: False | Key: False — Python standard library `logging` does not auto-mask tokens; it logs exact formatted strings)
- **Statement 4:** Correct (Answered: False | Key: False — `icecream` prints to stderr by default and does not secretly write to `app.log`)
- **Statement 5:** Correct (Answered: True | Key: True — Leaking tokens into logs or stdout compromises them even if `.env` is ignored by git)
- **Statement 6:** Correct (Answered: True | Key: True — Loading into environment variables only sets local process memory)
- **Statement 7:** Correct (Answered: False | Key: False — A token must be revoked or regenerated on GitHub's security settings to invalidate it server-side)

**Score:** 7 / 7 Correct (100%).
- **Status:** Security Hardening Gate passed.

---

## Checkpoint M2-8 Verification: Correctness Hardening (C-Gate)
**Date:** 2026-11-24

### Statements
1. Setting `per_page=100` on the GitHub `/users/{username}/repos` endpoint guarantees that a user with 150 repositories will receive all 150 repositories in a single HTTP response.
2. In Python, a default parameter defined as `payload: dict = {"cache": False}` is instantiated once at function definition time, meaning mutations to `payload` persist across subsequent calls where the caller does not supply that argument.
3. Calculating the total stars of a user by taking `len([repo for repo in repos if repo['stars'] > 0])` yields the exact same numerical result as summing the stargazers count across all repositories, provided every repository has at least one star.
4. When performing an integer modulo operation `time_diff %= 60`, the resulting value is mathematically guaranteed to be strictly in the range `0` to `59` (for non-negative integers).
5. A retry `while` loop with condition `while count < 3:` that performs a failing operation without incrementing `count` inside the loop body will continue executing indefinitely, consuming CPU cycles and freezing program exit.
6. HTTP status code `503 Service Unavailable` returned by an API server means that the client has sent too many requests in a given time window and must wait for `X-RateLimit-Reset`.
7. An API client that encounters an HTTP `404 Not Found` when requesting `/users/{username}/repos` can reliably conclude that the target user does not exist (or has no public presence), and should abort downstream reporting workflows rather than generating an empty success summary.

### Learner Response (Verbatim)
`f (in 2 payloads: 100 + 50), t, f, t, t, f, t`

### Evaluation
- **Statement 1:** Correct (Answered: False | Key: False — GitHub caps `per_page` at 100 maximum; 150 repos requires following pagination over 2 pages: 100 + 50)
- **Statement 2:** Correct (Answered: True | Key: True — Mutable defaults are created once at definition time and shared across invocations)
- **Statement 3:** Correct (Answered: False | Key: False — Even if every repo has stars, a repo with 5 stars adds 5 to the sum, but only 1 to the count)
- **Statement 4:** Correct (Answered: True | Key: True — Modulo 60 of any positive integer produces a remainder between 0 and 59)
- **Statement 5:** Correct (Answered: True | Key: True — Without incrementing the retry counter, the exit condition is never satisfied)
- **Statement 6:** Correct (Answered: False | Key: False — 503 is server error / temporary unavailability, whereas rate limits return 429 or 403)
- **Statement 7:** Correct (Answered: True | Key: True — A 404 indicates non-existence and downstream persistence should be aborted)

**Score:** 7 / 7 Correct (100%).
- **Status:** Correctness Hardening Gate passed.

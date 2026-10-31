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

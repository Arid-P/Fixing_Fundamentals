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

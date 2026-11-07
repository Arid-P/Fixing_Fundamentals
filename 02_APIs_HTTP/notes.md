# Milestone 02: Study Notes (Exportable to NotebookLM / Notewise)

## [Raw HTTP, URL Anatomy & Wire Flow]

- **The Mental Model:** An API call is not "opening a link"—it is a structured plain-text conversation over an operating system network socket (IP address + port number). The protocol operates like certified postal mail: DNS looks up the address, TCP ensures delivered in-order pages, TLS seals the envelope, and HTTP is the actual letter.
- **How it Works:**
  1. URL is parsed: `scheme://host:port/path?query#fragment`. Fragment is kept by the client; default ports are 80 (HTTP) or 443 (HTTPS).
  2. DNS resolves host to numeric IP.
  3. TCP completes the 3-way handshake (`SYN` -> `SYN-ACK` -> `ACK`) to open the socket.
  4. TLS negotiates symmetric encryption keys (for HTTPS).
  5. HTTP request is transmitted as plain text inside the TLS tunnel; exactly one response returns.
- **Ari's Code / Wire Inspection:**
  ```bash
  curl -i https://jsonplaceholder.typicode.com/posts/1
  # First line: HTTP/2 200 (protocol + status)
  # Followed by key-value headers, then an empty CRLF line (\r\n\r\n), then the JSON payload.
  ```
- **Common Pitfalls:**
  - Expecting the server to receive the fragment `#...` (client strips it).
  - Mixing up default ports: port 80 for HTTP, port 443 for HTTPS.
  - Assuming HTTP and HTTPS are different application languages (HTTPS is just HTTP inside a TLS pipe).


## [HTTP Anatomy, Methods & Status Codes]

- **The Mental Model:** HTTP communication is an explicit contract of messages. A Request specifies *what to do* (Method), *where to do it* (Path), *context* (Headers), and *data* (Body). A Response returns *what happened* (Status code), *metadata* (Headers), and *result* (Body).
- **How it Works:**
  1. **Request Line:** `[METHOD] [PATH] [HTTP_VERSION]` (e.g. `GET /posts/1 HTTP/1.1`).
  2. **Safe vs Idempotent:**
     - **Safe:** Does NOT mutate server state (read-only: `GET`, `HEAD`).
     - **Idempotent:** Calling it $N$ times leaves the server in the exact same state as calling it once (`GET`, `PUT`, `DELETE`). `POST` is NOT idempotent.
  3. **Status Families:**
     - `1xx`: Informational (protocol handshakes like `101 Switching Protocols` to WebSockets).
     - `2xx`: Success (`200 OK`, `201 Created`, `204 No Content`).
     - `3xx`: Redirection (`301 Moved Permanently`, `302 Found`).
     - `4xx`: Client Error (`400 Bad Request`, `401 Unauthenticated`, `403 Forbidden/No Permission`, `404 Not Found`, `405 Method Not Allowed`, `409 Conflict`, `422 Semantic Validation Failed`, `429 Rate Limited`).
     - `5xx`: Server Error (`500 Server Crashed`, `502 Bad Gateway / Upstream Died`, `503 Service Unavailable / Overloaded`).
- **Ari's Code / Wire Inspection:**
  ```bash
  curl -v https://jsonplaceholder.typicode.com/posts/1
  # > GET /posts/1 HTTP/2
  # > Host: jsonplaceholder.typicode.com
  # > User-Agent: curl/8.18.0
  # > Accept: */*
  # > [empty line indicates end of headers and no body]
  # < HTTP/2 200
  ```
- **Common Pitfalls:**
  - Believing `POST` is idempotent (running it multiple times creates duplicate resources or multiple transactions).
  - Confusing `401 Unauthorized` with `403 Forbidden` (`401` = unauthenticated/who are you?; `403` = authenticated but lack permission).
  - Thinking `204 No Content` is an error code (it is a success status that deliberately returns an empty payload body).

## [Python Requests: Methods, Params, Payloads & Headers]

- **The Mental Model:** The Python `requests` library abstracts the raw TCP/TLS socket into high-level Request and Response objects. Making a request produces a `Response` object `r` containing status, headers, and body.
- **How it Works:**
  1. **HTTP Verbs:** `requests.get()`, `requests.post()`, `requests.put()`, `requests.delete()`.
  2. **Query Parameters (`params=`):** Pass a dictionary to `params=`. `requests` automatically URL-encodes keys/values and appends them to the URL query string (`?key=val`).
  3. **Body Payloads (`json=` vs `data=`):**
     - `json={"key": "val"}`: Serializes Python dict to JSON string and sets header `Content-Type: application/json`.
     - `data={"key": "val"}`: Form-encodes data as `key=val` and sets header `Content-Type: application/x-www-form-urlencoded`. (Fails against strict JSON APIs with `422` or `400`).
  4. **Inspecting Outgoing vs Incoming:**
     - `r.headers`: What the server returned.
     - `r.request.headers`: What Python sent out across the wire.
     - `Content-Length`: Size of the payload body in raw bytes.
  5. **Response Handling:**
     - `r.status_code`: HTTP status as int (e.g. 200).
     - `r.text`: Response decoded to string.
     - `r.json()`: Parses `r.text` as JSON into Python dict/list (raises `json.JSONDecodeError` if invalid JSON).
     - `r.raise_for_status()`: Throws `HTTPError` on 4xx/5xx, no-op on 2xx/3xx.
- **Ari's Code:**
  ```python
  from requests import get, HTTPError

  url = "https://jsonplaceholder.typicode.com/posts"
  resp = get(url, params={"userId": 1})

  try:
      resp.raise_for_status()
  except HTTPError as e:
      print("Request failed:", e)
      exit()

  content = resp.json()
  for post in content:
      print(f"ID: {post['id']}, Title: {post['title']}")
  ```
- **Common Pitfalls:**
  - Manually concatenating query strings into the URL instead of using `params=` (fails with spaces, unicode, or special characters).
  - Passing a dict to `data=` when the API expects JSON (leads to `422 Unprocessable Entity`).
  - Assuming `.json()` is safe without checking status or catching JSON decode errors.

## [Network Resilience: Timeouts, Sessions, Retries & Errors]

- **The Mental Model:** The network is unreliable. Connections drop, servers freeze, and Wi-Fi glitches. Defensive network programming assumes failure is normal and handles timeouts, retries, and malformed data explicitly.
- **How it Works:**
  1. **Timeouts:** In `requests`, default timeout is `None` (waits forever). Always set `timeout=5.0`.
  2. **Connection Pooling (`requests.Session`):** Reuses the underlying TCP/TLS socket across requests via HTTP Keep-Alive, eliminating repeated handshakes.
  3. **Exception Hierarchy:**
     - `requests.ConnectionError`: DNS failure, refused connection, no internet.
     - `requests.Timeout`: Request exceeded `timeout=` limit.
     - `requests.HTTPError`: Server replied with 4xx or 5xx (raised by `.raise_for_status()`).
     - `requests.JSONDecodeError`: Body was not valid JSON (e.g. HTML captive portal / 500 error page).
  4. **Exponential Backoff:** Wait $2^{\text{attempt}}$ seconds (1s, 2s, 4s...) between retries to avoid overwhelming struggling servers.
  5. **Selective Retrying:**
     - Retry transient network errors (`ConnectionError`, `Timeout`) and transient server limits (`429`, `503`).
     - Never retry permanent client errors (`401 Unauthorized`, `404 Not Found`) or syntax errors.
     - Never wait on the final attempt before raising.
- **Ari's Code:**
  ```python
  def fetch_json(url: str, params: dict | None = None, max_retries: int = 3, timeout: float = 5.0):
      session = requests.Session()
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
              if resp.status_code in [429, 503]:
                  if retry == max_retries - 1:
                      raise
                  wait(retry)
              else:
                  raise
  ```
- **Common Pitfalls:**
  - Omitting `timeout` (causes program to hang indefinitely).
  - Assuming HTTP `200 OK` guarantees valid JSON data (captive portals return 200 with HTML).
  - Retrying `404` or `401` errors (they will never succeed without fixing URL or auth).
  - Sleeping on the final attempt before raising an error.


## [Real APIs, OpenAPI & Documentation Specs]

- **The Mental Model:** Markdown documentation quickly becomes stale when engineers change code. OpenAPI Specification (OAS) is the formal, machine-readable blueprint (JSON/YAML) of an API. Swagger UI is an interactive frontend automatically rendered from that blueprint.
- **How it Works:**
  1. **OpenAPI Spec:** Standardized schema listing paths, HTTP methods, required query/path parameters, and response schemas.
  2. **Swagger UI:** The web client (like `/docs` in FastAPI) generated from OAS allowing manual testing in browser.
  3. **Parameter Types:**
     - Query parameters (`?key=val`): filtering, pagination, coordinates.
     - Path parameters (`/users/{id}`): identifying a specific resource.
- **Ari's Code:**
  ```python
  params = {
      "latitude": 28.6139,
      "longitude": 77.2090,
      "current": "temperature_2m,weather_code",
      "daily": "temperature_2m_max,temperature_2m_min",
      "timezone": "auto",
  }
  resp = fetch_json(url="https://api.open-meteo.com/v1/forecast", params=params)
  ```
- **Common Pitfalls:**
  - Misspelling query parameter keys (e.g. `latidute` instead of `latitude`), which causes the server to ignore inputs or return empty payloads with `200 OK`.
  - Confusing Swagger UI (the webpage tool) with OpenAPI (the underlying specification).


## [API Pagination: Offset/Limit vs Cursor]

- **The Mental Model:** Servers cannot send millions of rows in one response. They slice data into pages. Offset pagination is like flipping page numbers in a book; cursor pagination is like bookmarking the exact ID/timestamp of where you stopped.
- **How it Works:**
  1. **Offset/Limit:** Client requests `limit=10&offset=0`. Page 2 is `limit=10&offset=10`.
     - *Flaw:* If items are inserted/deleted in real time, offsets shift, causing duplicate or skipped items.
  2. **Cursor / Keyset:** Server returns an opaque token (`cursor="id_123"`) representing the last item. Client requests `cursor="id_123"`.
     - *Benefit:* Stable against real-time insertions; $O(1)$ database query performance.
  3. **Following Next Links:** Many APIs (PokeAPI, GitHub) provide a `next` link directly inside the response headers or body.
- **Ari's Code:**
  ```python
  url = "https://pokeapi.co/api/v2/pokemon?limit=10&offset=0"
  for _ in range(page_count):
      resp = fetch_json(url=url)
      pages.append(resp.get("results"))
      url = resp.get("next")  # Server drives pagination
  ```
- **Common Pitfalls:**
  - Manually computing string offsets instead of consuming the server-provided `next` link.
  - Assuming an offset pagination query is cheap on millions of records (databases must scan and throw away $N$ rows).


## [Disk Caching with Metadata & TTL Invalidation]

- **The Mental Model:** The pantry pattern. Check local disk before heading out to the network store. If the food in the pantry is missing or expired (TTL), fetch fresh data and store it with a timestamp.
- **How it Works:**
  1. Check if the cache file exists on disk and is non-empty (`file.stat().st_size > 0`).
  2. Read cache file containing an envelope: `{"time": "<timestamp>", "response": {...}}`.
  3. Compute elapsed time: `time_diff = datetime.now() - saved_time`.
  4. If `time_diff` exceeds TTL threshold (e.g. $> 1$ day), treat as a cache miss.
  5. On cache miss: fetch from API, serialize to disk with `json.dump(..., default=str)`, return payload.
- **Ari's Code:**
  ```python
  def check_load_data(file: Path) -> dict | None:
      if (not file.exists()) or file.stat().st_size == 0:
          return None
      with open(file, 'r') as fh:
          content = load(fh)
      time_diff = dt.now() - dt.strptime(content.get('time'), '%F %T.%f')
      if time_diff.days > 1:
          return None
      return content.get('response')
  ```
- **Common Pitfalls:**
  - Calling `.touch()` or creating 0-byte files before checking existence, causing `JSONDecodeError` on subsequent reads.
  - Calling `.readline()` multiple times on an open file handle, which advances the stream pointer and starves `json.load()`.
  - Creating files in non-existent parent directories without `mkdir(parents=True, exist_ok=True)`.


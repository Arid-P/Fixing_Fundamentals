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

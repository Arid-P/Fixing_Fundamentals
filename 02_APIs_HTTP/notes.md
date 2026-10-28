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


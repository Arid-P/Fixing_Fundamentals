# Milestone 02: APIs and HTTP

## Goal
- What actually is a api, and how do server communicate using it.
- WHat is HTTP and its protocals 



## What I built
What api is. HTTP v/s HTTPS, a scoket, 

## What actually clicked
- **What actually Happens Between your device and server:** When your browser or a Python script talks to a server, it does not "open a link". It opens a network connection (TCP socket) to a remote computer and sends plain text formatted according to the HTTP specification. The server reads that text, processes it, and streams plain text back. 
    One request → exactly one response. The server cannot talk until spoken to, and once the response completes, that HTTP cycle is done. 

- **URL (Uniform Resource Locator) & Its Anatomy:** Before a request can go anywhere, the client needs a destination. URL provides that destination in form of a string. A URL is not just a string; it is broken down by the HTTP client into 6 distinct parts: 
    General Format: `scheme://host:port/path?query_string#fragment`
    | Component | Purpose | Example |
    |---|---|---|
    | **Scheme** | Protocol to communicate with | `https`, `http` |
    | **Host** | Domain name or IP address of the server | `jsonplaceholder.typicode.com`, `localhost` |
    | **Port** | Communication endpoint (default `80` for HTTP, `443` for HTTPS) | `:8000`, `:443` |
    | **Path** | Resource location on that server | `/posts/1`, `/docs` |
    | **Query String** | Key-value filters/parameters (starts with `?`, joined by `&`) | `?userId=1&sort=desc` |
    | **Fragment** | Internal page anchor (never sent across the wire to the server!) [Explanation](#url_fragment)| `#summary` |

- **DNS (Domain NameSystem - Application Layer):** It is like The Internet’s Phonebook but for IP address. DNS is a global distributed database. When you type a hostname, your OS asks DNS resolver for the IP, the resolver looks it up and returns IP so your computer knows whose door to knock on.

- **TCP (Transmission Control Protocol - Transport Layer):** It is a polite two-way radio check to maek sure that the connection is stable and works properly. It guarantees no lost packets and that bytes arrive in exact order. Before sending real data, client and server do a 3-step handshake best understood through the visual below. 
    ```text
    Client                                  Server
    |                                       |
    | -------- 1. SYN (Synchronize) ------> | "Hey, I want to talk. Can you hear me?"
    |                                       |
    | <------- 2. SYN-ACK (Acknowledge) --- | "Heard you loud and clear. Can you hear me?"
    |                                       |
    | -------- 3. ACK (Acknowledge) ------> | "Yes, I hear you. Let's begin."
    ```
    After its completion a stable bi dirction TCP socket is open.

- **TLS (Transport Layer Security - Cryptographic Wrapper):** It is to share the encryption key for the request's encryption scheme. TCP itself sends plain text. Anyone tapping the cable can read it. TLS does a cryptographic handshake over that TCP connection to establish a temporary secret encryption key about which both machines safely agree on. It also authenticates the server's identity (using SSL/TLS certificates) and verifies data integrity (ensuring packets aren't tampered with in transit).

- **HTTP (Application Layer):**  Over that encrypted TCP pipe established through TLS, your client finally sends plain text: GET /v1/forecast HTTP/1.1\r\nHost: api.open-meteo.com\r\n\r\n but encrypts using HTTPS. For more comhprehnsive understanding refer to [HTTP v/s HTTPS Point](#http_s). HTTP/1.1 sends plain text but HTTP/2 or /3 send binary framing with the exact same request/reponse semantics.

- **Socket:** A telephone plug in a specific apartment. *Analogy* Think of your computer as a apartment complex. It has a address (IP for the computer). Now for every program running represents a apratment, so the port n umber is like the apartment number. The computer uses this number to identify the reciever of a package (a packet) receved by it. 
            $Socket = IP Address + Port Number$
    So a Socket is just like a IP but for a specific program on your computr insteadof the whole computer.

- **:** 



## What I struggled with
- **Fragment in a URL**:<a id="url_fragment"></a> It is never actually end to the server. It is like a bookmark in a book you get from  library, where book is the reponse from the server and the library is the server. **The fragment identifier (defined in RFC 3986) is strictly client-side navigation. It instructs the client what to do with the resource after it has already arrived.** 
    _*Analogy:*_ Think of the server as a library and your browser as you holding the book. You ask the librarian: "Give me Volume 3" (that's the Path /v1/forecast). You don't tell the librarian: "Give me Volume 3 opened to page 45". The librarian only hands out whole books. Once the book is in your hands, you flip to page 45.

- **HTTP v/s HTTPS:**<a id="http_s"></a> Plain HTTP (Talking through an open window), it is simply the request's data without any encryption as plain english, which can be interrupted by anyone (your Wi-Fi router, an ISP, a hacker at a coffee shop). So HTTPS acts as the encryption. It encryptes that plain text and then send that so that it is not seen by anyone. <br> 
    ```HTTPS = HTTP (the language) placed inside TLS (the armored tunnel).``` <br> 
    *Analogy:* you shout that English sentence out your open window across the street to the server; The server understands it and shouts back the JSON; the problem is that anyone standing in the street can hear your exact words in plain text. So now instead of shouting out the window, you build a soundproof, encrypted glass-fiber pipe (TLS) directly between your room and the server. You speak the exact same HTTP sentence *inside* that pipe. The observer standing in the street only sees scrambled garbage (8a f3 01 bc...). When it reaches the server, TLS unscrambles it back to plain HTTP using the encryption shared during TLS.

- #### Networking Layers
    **The Mental Model:** The Postal Mail / Layer Cake. Each layer does exactly one isolated job so other layers don't have to care about it.

    | Layer | Protocol / Tech | Analogy / Single Job |
    |---|---|---|
    | **Application Layer** | HTTP, DNS | **The Letter:** The actual message/grammar (`GET /posts/1`). Doesn't know or care how bits travel. |
    | **Security Wrapper** | TLS (HTTPS) | **The Wax Seal / Armor:** Encrypts the letter so intermediaries cannot read it. |
    | **Transport Layer** | TCP | **Certified Delivery:** Tracks packets, numbers them, ensures none are lost, reassembles in order. |
    | **Network / Internet Layer** | IP | **The Envelope Address:** Routes packets from source IP to destination IP across routers. |
    | **Data Link / Physical Layer** | Wi-Fi, Ethernet, Fiber | **The Truck & Road:** Physical radio waves or electrical pulses moving across wires. |
    
    $*$ *(adapted from notes.md)*

- 28 Oct: thought http:// defaults to 443, it's 80 (443 is for https://).

## Open questions / revisit later
None.


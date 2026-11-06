# Milestone 02: APIs and HTTP

## Goal
- What actually is a api, and how do server communicate using it.
- WHat is HTTP and its protocals 



## What I built
What api is. HTTP v/s HTTPS, a scoket, 

## What actually clicked
- **What actually Happens Between your device and server:** When your browser or a Python script talks to a server, it does not "open a link". It opens a network connection (TCP socket) to a remote computer and sends plain text formatted according to the HTTP specification. The server reads that text, processes it, and streams plain text back. 
    One request → exactly one response. The server cannot talk until spoken to, and once the response completes, that HTTP cycle is done. 

- **URL (Uniform Resource Locator) & Its Anatomy:** Before a request can go anywhere, the client needs a destination. URL provides that destination in form of a string. A URL is not just a string; it is broken down by the HTTP client into 6 distinct parts: <a id="url"></a>
    General Format: `scheme://host:port/path?query_string#fragment` 
    | Component | Purpose | Example |
    |---|---|---|
    | **Scheme** | Protocol to communicate with | `https`, `http` |
    | **Host** | Domain name or IP address of the server | `jsonplaceholder.typicode.com`, `localhost` |
    | **Port** | Communication endpoint (default `80` for HTTP, `443` for HTTPS) | `:8000`, `:443` |
    | **Path** | Resource location on that server | `/posts/1`, `/docs` |
    | **Query String** | Key-value filters/parameters (starts with `?`, joined by `&`) | `?userId=1&sort=desc` |
    | **Fragment** | Internal page anchor (never sent across the wire to the server!) [Explanation](#url_fragment)| `#summary` |

#### What Actually happens behind the seen between the device and server initially.
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

> Refer to [Responses File to properly see exactly what I am using in examples](/02_APIs_HTTP/response.md#L90) But temporary consider what is shown below
```txt
> GET /posts/1 HTTP/2
> Host: jsonplaceholder.typicode.com
> User-Agent: curl/8.18.0
> Accept: */*
> 
```

- **Response Line:** It has 3 parts: [The Method](#Method) (GET), The Path, and the Protocaol Version. `[METHOD] [PATH] [HTTP_VERSION]`
    ```txt
    > GET /posts/1 HTTP/2
    ```

- **Headers:** The Headers are the key-value pairs that follow underneath the request line. It contain information regarding the client/host.
    ```txt
    > Host: jsonplaceholder.typicode.com
    > User-Agent: curl/8.18.0
    > Accept: */*
    ```

- **The Request Body:** It is the content that we send to the server besides information like path, path, etc. In our case it is empty `> `.


- **Methods:** <a id="Method"></a> It tells what is the action for when the request has been sent. It is of 5 main types given below but before that we must understand safe and idempotent. **Safe** is when the severs state isn't altered (db /cache etc. not updated), like retrieving data. **Idempotent** is when number of requests send doesn't matter as the result will be exactly like if only one request was sent, like pressing the elevator button, the number of times doesn't matter.  
    | Method | Primary Purpose | Has Request Body? | Safe? | Idempotent? |
    |---|---|---|---|---|
    |GET|**Retrieve** Resource|No|Yes|Yes|
    |POST|**Create** a new resorce or to perform some process|Yes|No|No|
    |PUT|Replace an entire resource or create another one but with the exact same id|Yes|No|Yes|
    |PATCH|Partially **update** an existing resource.|Yes|No|No (usually)|
    |Delete|**Remove** a Resource|No (usually)|No|Yes|

#### Status Codes' Families

- **Families:** Every HTTP response starts with a 3-digit numeric code. The first digit tells you the broad family, which are given below:
    |Family|Name|What it means| 
    |---|---|---|
    |1xx |Informaional|Protocol handshake in progress. Eg. [101 Switching Protocols](#L92). These are hardly used in `requests`|
    |2xx |Success|The request was recieved by the server successfully, understood and accepted|
    |3xx |Redirection|The resource that you are tryignto access lives somewhere else so go there|
    |4xx |Client Error|Fault form the users side. A bad request, invalid parameters, headers missing, etc|
    |5xx |Server Error|Server's Fault . Eg. backend crashed, database unreachable, gateway died, etc|  

    - *101 Switching Protocols:* HTTP is like a walki talkie and a one ay at that. Until it sends some request the server cannot respond. But formultiplayer and several other cases these is not feasible. So we establish a persistent two communication design where either side can send requests any time. These are know as Websockets. But the browser cannot esatbli8sh them by default, so it first of all requests server for it and if it agrees then server replies `HTTP/1.1 101 Switching Protocols` 

- **The Success Trio (200, 201, 204):**  
    - *`200:`* Standard Success. Everything went as it should have and it retyrnee what was asked for;  
    - *`201 Created:`* Typically for POST, the resources was created;  
    - *`204 No Content:`* Typically fr DELETE, the action was successfully performed but there is nothing to return.

- **Redirection (301, 302):**   
    - *`301 Moved Permanently:`* The URL changed forever. Clients and search engines cache the new URL and won't ask the old one again.;  
    - *`302 Found (Temporary Redirect):`* The resource is temporarily at a different location for this request only.  

- **Client Errors (400, 401, 403, 404, 405, 409, 422, 429):** 
    - *`400 Bad Request:`* Whatever the request was it was not proper. Eg.,broken JSON syntax that can't be parsed.
    - *`401 Unauthorised:`* More accurately **Unauthenticated**. The server cannot identify you, "Who are you?"
    - *`403 Forbidden:`* Authenticated, but no permission. "I know who you are, but you are not an Admin". Something like banned or some user trying to login but into wrong level.
    - *`404 Not Found:`* The URL path does not exist on the server.
    - *`405 Method Not Allowed:`* The path exists but the Method or the action is not defined/implemented yet.
    - *`409 Conflict:`* Edit conflict (like in git) or duplicate ntry (trying to create two accounts with the same email)
    - *`422 Unprocessable Entity:`* The Json was prased but the data values within it are wrong/invalid and could not be processed (eg age: -19)
    - *`429 Too Many requests:`* Rate limit Exceeded.

- **Server Errors (500, 502, 503):** 
    - *`500 Internal Server Error:`* Some error in the server crashed it. More appropriately an unhandled exception crashed the backend code (e.g., Python threw an unhandled ZeroDivisionError).
    - *`502 Bad Gateway:`* The reverse proxy (Cloudflare) contacted the backend app (uvicorn), but backend dint return valid data or was down.
    - *`503 Service Unavailable:`* Exactly as the name suggests. E.g. The server is temporarily overloaded or undergoing maintenance.


#### Python `requests` Module
- **Response Object:** When we use request module, we call or sent the request using `requests.get(...)`. This does not return text or JSON instead it returns everything in a `Response` object. So we use methods to aces different values form the object.

- **Methods & Attributes of `Response` Object:**
    - *`obj.status_code() -> int`*: Gives an integer representing the HTTP status code (200, 404, etc)
    - *`obj.headers() -> dict`*: A case-insensitive dictionary of response headers sent by the server.
    - *`obj.text() -> str`*: The raw response as a Python `str`, the decoding of the content is according to whatever is specified when calling `get`.
    - *`obj.json() -> dict | list`*: It passes `obj.text()` as JSON and returns a Python `dict` or `list`. *Pitfall: if the server returned HTML or plain text, calling .json() crashes with a JSONDecodeError*
    - *`obj.raise_for_status() -> `*: An essential error-check method. If the status code is `4xx` or `5xx`, i.e., some error has occured, it raises an HTTPError. If the response is `2xx`/`3xx`, it silently does nothing.

- **Path Params vs Query Params vs Body:** Here we will see where the data goes when we call an api.
    |Type|Where It Goes<br>[URL Format](#url)|When To Use|How in `requests`|
    |---|---|---|---|
    |Path Parameter|In the URL path, after the port (or host) (`/post/1`)|To identify a specific resource|Build into the URL string|
    |Query Parameter|After the `?`, i.e., after the path (`/posts?userId=1`)|To apply some conditions to the query, like filter, sort etc|Pass a `dict` to `params=` option.|
    |Body (Payload)|After the header blank line|Submitting data along in the string|Pass to `json=` or `data`|

- **Request `json=` v/s `data=`:** The payload that the user sents to the server is stream of bytes, so the server needs to know how to comprehend it. Now `json=` automatically tells `requests` to convert the data into a json string (`json.dumps`) and sets the `Content-Type: application/json` for the sever. Whereas `data=` means that `request` can convert the Python `dict` into URL-encoded key value pairs (`'title=hello&userId=1'`), and sets `Content-Type: application/x-www-form-urlencoded` mimicking an old-school browser HTML `<form>`.
    >Error Occurrence:
    >If a modern API expects a JSON body and you use `data=` the server cannot parse it as JSON and will reject it with `422 Unprocessable Entity` or `400 Bad Request`! So if the api accepts json just use `json=`

- **`response.request.headers/body`:** It is to check the content of the request that was sent from the user's side. `response.headers` returns the headers of the response that the server sent. It is best used in debugging to check if you actually sent the proper request.

- **Always Setting Timeouts:** In `requests` there is no default timeout, ie, it is `None`. But in reality this is very dangerous, like in some scenario it can take a minute or two for the response to return, letting a request live for this long is very dangerous. So we use `timeout` argument. In it, we provide the time period in seconds. Or we can also use the format `(connect_timeout, rerad_timeout)` to be more precise. E.g.:
    ```py
    requests.get("https://...", timeout=5.0)
    ```

- **Major Error in `requests`:** All network exceptions in requests inherit from `requests.RequestException`. The 4 major types are:
    |Name|Why it Occurs|
    |---|---|
    |`requests.ConnectionError`|There is no internet connection, o9r the DNS lookup for the IP failed, or simply a connection refused|
    |`requests.Timeout`|When the server takes longer to responsed than the `timeout=` time period set.|
    |`requests.HTTPError`|Raised by `resp.raise_for_status()` when the status code is `4xx/5xx`|
    |`json.JSONDecdeError` (from the standard library `json`)|Upon calling `.json()` but the reponse4 body has no valid JSON.|

    An example for a script's output:
    ```txt
    ic| name: 'connection'
        content: ConnectionError(MaxRetryError('HTTPSConnectionPool(host=\'domain-dne.com\', port=443): Max retries exceeded with url: /args (Caused by NameResolutionError("HTTPSConnection(host=\'domain-dne.com\', port=443): Failed to resolve \'domain-dne.com\' ([Errno -2] Name or service not known)"))'))
    
    ic| name: 'timeout'
        content: ReadTimeout(ReadTimeoutError("HTTPSConnectionPool(host='httpbin.org', port=443): Read timed out. (read timeout=1.5)"))

    ic| name: 'http'
        content: HTTPError('404 Client Error: Not Found for url: https://jsonplaceholder.typicode.com/posts/999999')
    
    ic| name: 'json'
    content: JSONDecodeError('Expecting value: line 1 column 1 (char 0)')
    ```

- **HTTP 200 Does NOT Mean Valid Data!:** 200 is to tell that the request was a success and the server was able to process it and respond. It never means that there is data that we can read. 
    - It can return nothing,
    - Or maybe a login page asking you to accept terms and condition, etc;
    - More importantly, if you are using a legacy API, then you can encounter instances where even error messages come with a `200 OK` and a body like: {"status": "error", "message": "User not found"}.
    - ***What to do:*** Use `status_code` or `raise_for_status()` to first ensure that the request was a success, __and__ wrap `.json()` within a `try...except` and __validate the data keys__.

- **`requests.Session`:** Every time we use `get()` the whole process from DNS lookup to the closing of socket takes place for a single process. So 50 API calls means the whole cycle repeating 50 times, resulting in a lot of waste.  
    So to resolve this we use `Session()` to establish the connection along with the socket only once, and utilize it for a number of API calls. This results in the request being 3x to 5x faster. It also preserves cookies and default headers across requests.

- **Retry with Exponential Backoff:** In any case like API overload (429, 503), or when a packet drops, or some error occurs, you don't just immediately crash and show that request failed, nor, continuously request the server. Instead, we implement __Exponential Backoff__:
    - Try request (attempt 0). If it fails wait 1s (${2}^{0}$) befoe the next try,
    - Try request (attempt 1). If it fails wait 2s (${2}^{1}$) befoe the next try,
    - Try request (attempt 2). If it fails wait 4s (${2}^{2}$) befoe the next try, ...;
    - If the requests keep failing we keep trying till max retries (set by us), then give up, and report an error.

- **Header:** 




## What I struggled with
- **Fragment in a URL**:<a id="url_fragment"></a> 
    - It is never actually end to the server. It is like a bookmark in a book you get from  library, where book is the reponse from the server and the library is the server. 
    - **The fragment identifier (defined in RFC 3986) is strictly client-side navigation. It instructs the client what to do with the resource after it has already arrived.**   
    - _*Analogy:*_ Think of the server as a library and your browser as you holding the book. You ask the librarian: "Give me Volume 3" (that's the Path /v1/forecast). You don't tell the librarian: "Give me Volume 3 opened to page 45". The librarian only hands out whole books. Once the book is in your hands, you flip to page 45.

- **HTTP v/s HTTPS:**<a id="http_s"></a> 
    - Plain HTTP (Talking through an open window), it is simply the request's data without any encryption as plain english, which can be interrupted by anyone (your Wi-Fi router, an ISP, a hacker at a coffee shop). 
    - So HTTPS acts as the encryption. It encryptes that plain text and then send that so that it is not seen by anyone. <br> 
    ```HTTPS = HTTP (the language) placed inside TLS (the armored tunnel).``` <br> 
    - *Analogy:* you shout that English sentence out your open window across the street to the server; The server understands it and shouts back the JSON; the problem is that anyone standing in the street can hear your exact words in plain text. So now instead of shouting out the window, you build a soundproof, encrypted glass-fiber pipe (TLS) directly between your room and the server. You speak the exact same HTTP sentence *inside* that pipe. The observer standing in the street only sees scrambled garbage (8a f3 01 bc...). When it reaches the server, TLS unscrambles it back to plain HTTP using the encryption shared during TLS.

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

- 5 Nov: Struggled slightly with `json=`, `data=`.

## Open questions / revisit later
- Networking Layers at the hardware level.


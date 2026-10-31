### curl -i https://jsonplaceholder.typicode.com/posts/1
```txt
HTTP/2 200 
date: Wed, 28 Oct 2026 14:55:42 GMT
content-type: application/json; charset=utf-8
content-length: 292
access-control-allow-credentials: true
cache-control: max-age=43200
etag: W/"124-yiKdLzqO5gfBrJFrcdJ8Yq0LGnU"
expires: -1
pragma: no-cache
vary: Origin, Accept-Encoding
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 3600000
x-ratelimit-remaining: 3599999
x-ratelimit-reset: 1790812826
accept-ranges: bytes
nel: {"report_to":"cf-nel","success_fraction":0.0,"max_age":604800}
age: 18255
cf-cache-status: HIT
report-to: {"group":"cf-nel","max_age":604800,"endpoints":[{"url":"https://a.nel.cloudflare.com/report/v4?s=cTuLEvHHu7IpI9MPYiLP1wMG4n%2BRei63NN6%2F3R7xwOO3BKrpuQ2eQDvYXKnuo8JW%2FYF7KpocuIGbGbPnxVoGT4IlKzubsjCfAunHJE8uvD%2B36jUWmcQOQ6FOxvx4PPTLMq%2F3bcshcFdAZ8LMBdbweTYb2rOdSNxukCZX"}]}
server: cloudflare
cf-ray: a51ac86f7f55fe23-SIN
alt-svc: h3=":443"; ma=86400

{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
```

### curl -v https://jsonplaceholder.typicode.com/posts/1
```txt
  % Total    % Received % Xferd  Average Speed  Time    Time    Time   Current
                                 Dload  Upload  Total   Spent   Left   Speed
  0      0   0      0   0      0      0      0                              0* Host jsonplaceholder.typicode.com:443 was resolved.
* IPv6: 2606:4700:3033::6815:3b13, 2606:4700:3037::ac43:a797
* IPv4: 172.67.167.151, 104.21.59.19
*   Trying [2606:4700:3033::6815:3b13]:443...
*   Trying 172.67.167.151:443...
* ALPN: curl offers h2,http/1.1
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [1583 bytes data]
* SSL Trust Anchors:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
*   CApath: /etc/ssl/certs
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [1210 bytes data]
* TLSv1.3 (IN), TLS change cipher, Change cipher spec (1):
{ [1 bytes data]
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
{ [19 bytes data]
* TLSv1.3 (IN), TLS handshake, Certificate (11):
{ [2490 bytes data]
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
{ [79 bytes data]
* TLSv1.3 (IN), TLS handshake, Finished (20):
{ [52 bytes data]
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.3 (OUT), TLS handshake, Finished (20):
} [52 bytes data]
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384 / X25519MLKEM768 / id-ecPublicKey
* ALPN: server accepted h2
* Server certificate:
*   subject: CN=typicode.com
*   start date: Sep 27 01:17:47 2026 GMT
*   expire date: Dec 26 02:17:39 2026 GMT
*   issuer: C=US; O=Google Trust Services; CN=WE1
*   Certificate level 0: Public key type EC/prime256v1 (256/128 Bits/secBits), signed using ecdsa-with-SHA256
*   Certificate level 1: Public key type EC/prime256v1 (256/128 Bits/secBits), signed using ecdsa-with-SHA384
*   Certificate level 2: Public key type EC/secp384r1 (384/192 Bits/secBits), signed using ecdsa-with-SHA384
*   subjectAltName: "jsonplaceholder.typicode.com" matches cert's "*.typicode.com"
* SSL certificate verified via OpenSSL.
* Established connection to jsonplaceholder.typicode.com (2606:4700:3033::6815:3b13 port 443) from 2405:201:600e:907c:288:1de5:f95:7771 port 42636 
* using HTTP/2
* [HTTP/2] [1] OPENED stream for https://jsonplaceholder.typicode.com/posts/1
* [HTTP/2] [1] [:method: GET]
* [HTTP/2] [1] [:scheme: https]
* [HTTP/2] [1] [:authority: jsonplaceholder.typicode.com]
* [HTTP/2] [1] [:path: /posts/1]
* [HTTP/2] [1] [user-agent: curl/8.18.0]
* [HTTP/2] [1] [accept: */*]
} [5 bytes data]
> GET /posts/1 HTTP/2
> Host: jsonplaceholder.typicode.com
> User-Agent: curl/8.18.0
> Accept: */*
> 
* Request completely sent off
} [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
{ [230 bytes data]
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
{ [230 bytes data]
< HTTP/2 200 
< date: Sat, 31 Oct 2026 07:22:00 GMT
< content-type: application/json; charset=utf-8
< content-length: 292
< access-control-allow-credentials: true
< cache-control: max-age=43200
< etag: W/"124-yiKdLzqO5gfBrJFrcdJ8Yq0LGnU"
< expires: -1
< pragma: no-cache
< vary: Origin, Accept-Encoding
< x-content-type-options: nosniff
< x-powered-by: Express
< x-ratelimit-limit: 3600000
< x-ratelimit-remaining: 3599999
< x-ratelimit-reset: 1790812826
< accept-ranges: bytes
< nel: {"report_to":"cf-nel","success_fraction":0.0,"max_age":604800}
< age: 19834
< cf-cache-status: HIT
< report-to: {"group":"cf-nel","max_age":604800,"endpoints":[{"url":"https://a.nel.cloudflare.com/report/v4?s=rATCzTooz0TjmiY8Cm3lS7r23LNvwpCjHSwFiW%2FvqNhqfoXR%2FiZXSj30Zef5g%2Bg2gzwOgL8iFZolB2%2FsUEmZBlDJM5jVh4bFfo6mDSjcePbFn12v1eGOtZnqzt333kkACqM9pztnPTC9%2FzA3P657lI5hLeantGdzRD2I"}]}
< server: cloudflare
< cf-ray: a530e7fb0ad5f8c6-SIN
< alt-svc: h3=":443"; ma=86400
< 
{ [5 bytes data]
100    292 100    292   0      0    414      0                              0
* Connection #0 to host jsonplaceholder.typicode.com:443 left intact
```



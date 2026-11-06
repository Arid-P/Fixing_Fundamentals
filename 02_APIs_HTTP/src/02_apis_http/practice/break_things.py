from requests import get, post, HTTPError, Timeout, ConnectionError, JSONDecodeError
from icecream import ic

errors = {}

try:
    resp = get(r"https://domain-DNE.com/args")
except ConnectionError as e:
    print(f"The Connection error has occured.")
    errors["connection"] = e

try:
    resp = get(r"https://httpbin.org/delay/5", timeout=1.5)
except Timeout as e:
    print(f"The Timeout error has occured.")
    errors["timeout"] = e

try:
    resp = get(r"https://jsonplaceholder.typicode.com/posts/999999")
    resp.raise_for_status()
except HTTPError as e:
    print(f"The HTTP error has occured.")
    errors["http"] = e

try:
    resp = get(r"https://httpbin.org/html")
    resp.json()
except JSONDecodeError as e:
    print(f"The JSON decode error has occured.")
    errors["json"] = e

print()

for name, content in errors.items():
    ic(name, content)

"""
For refrence:
ic| name: 'connection'
    content: ConnectionError(MaxRetryError('HTTPSConnectionPool(host=\'domain-dne.com\', port=443): Max retries exceeded with url: /args (Caused by NameResolutionError("HTTPSConnection(host=\'domain-dne.com\', port=443): Failed to resolve \'domain-dne.com\' ([Errno -2] Name or service not known)"))'))
ic| name: 'timeout'
    content: ReadTimeout(ReadTimeoutError("HTTPSConnectionPool(host='httpbin.org', port=443): Read timed out. (read timeout=1.5)"))
ic| name: 'http'
    content: HTTPError('404 Client Error: Not Found for url: https://jsonplaceholder.typicode.com/posts/999999')
ic| name: 'json'
    content: JSONDecodeError('Expecting value: line 1 column 1 (char 0)')
"""
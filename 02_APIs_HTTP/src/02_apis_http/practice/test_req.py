import requests

# in place of ambiguis r we will use response or resp

response: requests.Response = requests.post(
    "https://jsonplaceholder.typicode.com/posts", json={"title": "hello", "userId": 1}
)

print("Status:", response.status_code)
print("Request Headers (some part):", response.request.headers)
print("Request Headers (request part):", response.request)
print("Request Headers (full):", response.headers)

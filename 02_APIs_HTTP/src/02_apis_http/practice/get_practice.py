from requests import get, HTTPError
from icecream import ic

ic.disable()

url = r"https://jsonplaceholder.typicode.com/posts"
resp_post = get(url, params={"userId": 1})

try:
    resp_post.raise_for_status()
except HTTPError as e:
    print("The request was not suucessful")
    ic(e)
    exit()

content = resp_post.json()
ic(content)
print("The response:\n")

for resp in content:
    print("The first dict")
    for key, val in resp.items():
        print(f"{key}: {val}")
    print()

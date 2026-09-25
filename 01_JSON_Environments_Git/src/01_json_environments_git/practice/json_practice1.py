import json
from pathlib import Path


BASE_DIR = Path('.', 'src', '01_json_environments_git')
USER_PATH = BASE_DIR / 'data' / 'users.json'
OUTPUT_PATH = BASE_DIR / 'practice' / 'output.json'

users: list[dict] = []

#TODO 1: Opens and loads users.json using the appropriate json file-reading method.

with open(USER_PATH, 'r') as json_fh:
    users = json.load(json_fh)


#TODO 2: Iterates over the users and prints each user's name, their city, and their company name in a clean format 
# E.g., Leanne Graham lives in Gwenborough and works at Romaguera-Crona.

for user in users:
    name = user["name"]
    city = user["address"]["city"]
    company_name = user.get("company").get("name")
    print(f"{name} lives in {city} and works at {company_name}.")

print()


#TODO 3: Demonstrates json.dumps() by taking the first user's dictionary and converting it into a formatted JSON string with an indentation of 2 spaces, and printing that string.
#Give an example so i understand better, but i am still trying so check that as well.

user = users[0]
formatted_string = json.dumps(user, indent=2)
print(formatted_string)
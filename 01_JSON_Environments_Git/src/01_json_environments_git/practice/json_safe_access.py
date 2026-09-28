from json import load, dump
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
USERS_PATH = BASE_DIR / 'data' / 'users.json'

#Loading users.json
with open(USERS_PATH, 'r', encoding='utf-8') as file:
    users = load(file)


#Adding a dummy user with corruptful data
users.append({
    "id": 34234,
    "name": "Corrupted User",
    "address": None,
})


for user in users:
    name = user.get('name')
    city = (user.get('address') or {'city': 'N/A'} ).get('city')
    #If get() returns None then the other value is used

    company_name = (user.get('company') or {'name': 'Freelance'} ).get('name')
    try: #I am not writing nested dictionary
        latidtude = float(user['address']['geo']['lat'])
    except (KeyError, TypeError):
        latidtude = 0.0

    print(f"{name} lives in {city} ({latidtude}), and works for/as {company_name}.")


from pathlib import Path
from csv import DictReader, DictWriter
from json import load, dump

BASE_DIR = Path('.', 'src', '01_json_environments_git')
USER_JSON_PATH = BASE_DIR / 'data' / 'users.json'
USER_CSV_PATH = BASE_DIR / 'data' / 'users.csv'
OUTPUT_PATH = BASE_DIR / 'data' / 'users_from_csv.json'

with open(USER_JSON_PATH, 'r') as file:
    users = load(file)

data = []
keys = ['id', 'name', 'email', 'city']
for user in users:
    data.append({"id": user["id"], "name": user["name"], "email": user["email"], "city": user["address"]["city"]})

with open(USER_CSV_PATH, 'w', newline='', encoding='utf-8') as file:
    writer = DictWriter(file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(data)


#TASK 02: CSV to JSON
with open(USER_CSV_PATH, 'r') as file:
    rows = list(DictReader(file))

with open(OUTPUT_PATH, 'w') as file:
    dump(rows, file, indent=2)


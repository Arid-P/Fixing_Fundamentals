from json import loads, dump, dumps, JSONDecodeError
from pathlib import Path
from datetime import datetime
from shutil import copy
from os import replace

#to debug
from icecream import ic

BASE_DIR = Path(__file__).parent.parent
USERS_PATH = BASE_DIR / 'data' / 'users.json'
TODOS_PATH = BASE_DIR / 'data' / 'todos.json'


invalid_data = '{"name": "Ari", "status": incomplete,}'

try:
    data_dump = loads(invalid_data)
except JSONDecodeError as err:
    print(f"The error: {err.msg}, occured at line number: {err.lineno} and at column: {err.colno}")


#How do i insert the datetime and path obj?
data_dt = {
    "name": "Ari", 
    "completed": "False", 
    "Path": USERS_PATH, 
    "created_at": datetime.now(),
    "symbol": "₹"  
}

out_str = dumps(data_dt, indent=4, ensure_ascii=True, default=str)
print(out_str)


    #I am supossing the data already formatted to be dumped
def atomic_json_dump(data, target_path: Path) -> None:
    BACKUP_FILE = target_path.parent / f'{target_path.name}.bak'
    TEMP_FILE = target_path.parent / f'{target_path.name}.tmp'

    #creating backup    
    target_path.parent.mkdir(parents=True,exist_ok=True)

    #To make sure the file exists
    if target_path.exists():
        copy(target_path, BACKUP_FILE)    

    #writing to temp
    with open(TEMP_FILE, 'w') as file:
        dump(data, file, indent=4, default=str)

    replace(TEMP_FILE, target_path) 

test_file = BASE_DIR / 'data' / 'test_robust.json'
atomic_json_dump(data_dt, test_file)
print("Saved successfully!")

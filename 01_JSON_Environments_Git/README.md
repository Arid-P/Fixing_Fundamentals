# Milestone 01: JSON and Git Merge Conflicts.

## Goal

1. What is JSON, how we read and undersytand it. 
2. How we handle JSON files, extracting data, writting data, and other operations, using python.
3. Under standing merging, the different  conflicts which can arise, methods to resolve these conflicts and some advanced git. 

## What I built
- **`process_todos.py`:** It takes the users and todos from `users.json`, `todos.js`respectively and aggregates the todo which each user has and displays it. It also gives you the option to add a new todo.

## What actually clicked
- **`json.load()`:** If you have a json file (or something from which you can read json from, it should not be a python string) then you can use this `json.load(``obj``)` to load the json from it as a list of dictionaries into python. For example:
    ```python
    with open('<file_paht>/<file_name>.json', 'r') as json_fh:
        users = json.load(json_fh) #file hndlder
    ```


- **`json.load_s_()`:** Just `json.load` but for python strings. For example:
    ```python
    raw_json_str = '{"name": "Ari", "milestone": 1}'
    data = json.loads(raw_json_str)
    ``` 


- **`json.dump()`:** It is the inverse of `json.load()`. If you have a pyhtonic object like `dict` or `list` in proper format that we want to tranform into a json format data, then we can use it. For example:
    ```python
    user_details = {'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}}

    with open('<file_path>/<file_name>.py' , 'w') as file:
        json.dumps(user_details, file, indent=2) #dumps the user as a formatted data into the file
    ```


- **`json.dump_s_()`:** Exactly like `json.dump()` but to get a formatted string. It takes a pythonic object as input and return a string. For example:
   ```python
    user_details = {'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}}

    formatted_string = json.dumps(user_details, indent=2)
    print(formatted_string) #dumps the user as a formatted string variable
    ```


- **`json.load()`:**

- **`json.load()`:**

- **`json.load()`:**

- **`json.load()`:**


## What I struggled with
- json.dumps. Now it is ok.

## Open questions / revisit later
None
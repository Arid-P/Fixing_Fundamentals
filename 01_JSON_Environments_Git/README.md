# Milestone 01: JSON and Git Merge Conflicts.

## Goal

1. What is JSON, how we read and undersytand it. 
2. How we handle JSON files, extracting data, writting data, and other operations, using python.
3. Under standing merging, the different  conflicts which can arise, methods to resolve these conflicts and some advanced git. 

## What I built
- **`process_todos.py`:** It takes the users and todos from `users.json`, `todos.js`respectively and aggregates the todo which each user has and displays it. It also gives you the option to add a new todo.

## What actually clicked
- **`json.load()`:** If you have a json file (or something from which you can read json from, it should not be a python string) then you can use this `json.load(obj)` to load the json from it as a list of dictionaries into python. For example:
    ```python
    with open('<file_paht>/<file_name>.json', 'r') as json_fh:
        users = json.load(json_fh) #file hndlder
    ```


- **`json.load_s_()`:** Just `json.load` but for python strings. The keys must be in double quotes and the whole expression in single quote. For example:
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


- **`python -m json.tool <file_path>/<file_name>`:** It is supposed to be ran in a *terminal*. It checks if all the keys within the file are proper and the values asssociated with each are also allowed ones. It automatically pretty prints the file's contents.

- **Safe key access:** Use .get() and .upate() methods to get dafely get the values from the dictionary or use `try: ... except: ...` blocks. FOr example:
    ```python
    for user in users:
        name = user.get('name')
        city = (user.get('address') or {'city': 'N/A'} ).get('city')
        #If get() returns None then the other value is used

        company_name = (user.get('company') or {'name': 'Freelance'} ).get('name')
        try: #I am not writing nested dictionary
            latidtude = float(user['address']['geo']['lat'])
        except (KeyError, TypeError):
            latidtude = 0.0
    ```

- **Filter, Sort & Group:** Use `sorted(iterable, key)` function, `collections.Counters(iterable)` and `collections.defaultdict(<default_data_type>)` methods for grouping. `filter()` function for filtering. You can use other common iterable techniqes.

- **Good Practice for Failure** Sometimes while dumping data into a file with `'w'`, the process could become corrupted, or may the connection to the server fail, in such a such situation now you have a file with either no data or no data at all. Hence to prevent this we follow:
        1. *Backup*: Make a backup of the file to be wriiten on (`data.json.bak`)
        2. *Write to Temp*: Make a temperory file (`data.json.tmp`) and write the data on it
        3. *Replace*: Replace the original file with the temp file. Use `os.replace(temp_file, target_file)`. 

- **`json.JSONDecodeError`:** It occurs when you process a bad syntax json file, like file provided by the user, or a network, json. Then using this error, we ca figure out the *line number* using `err.lineno`, *exact column* using `err.colno`, *the message* using `err.msg` (the rule violated, it is in double quotes).

- **Serialization Flags:** They are some flags we can use with `json.dump()` and `json.dumps()`. These include: 
        - `sort_keys=True`: Sorts dictionary keys alphabetically.
        - `ensure_ascii=False`:  By default, Python converts non-ASCII characters (emojis, Hindi, accents) into escape codes (\u20b9). Setting ensure_ascii=False writes the actual UTF-8 characters cleanly.
        - `default=str`: It converts all the different data types present in the data to str, like if `datetime` or `Path` obj is present then it automatically converts it into a str.

###Use of JSON Along with CSV
- **``:**
- **``:**
- **``:**
- **``:**


## What I struggled with
- json.dumps. Now it is ok.

## Open questions / revisit later
None
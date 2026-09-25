# Milestone 01 Study Notes: JSON and Git Merge Conflicts

## JSON Serialization & Deserialization
- **The Mental Model:**
  - **In-Memory vs. On-Disk/Wire**: Python dictionaries, lists, and integers live as dynamic memory objects in RAM. When you want to store them on disk or transmit them across a network (e.g., to/from a REST API), you must convert them into a standardized, universally understood text format (JSON).
  - **"Dumping" (Serialization)**: Packing in-memory Python data structures into formatted JSON text strings or writing them into a file.
  - **"Loading" (Deserialization)**: Unpacking JSON text strings or file contents back into native Python dictionaries and lists.
  - **The `s` rule**: Any method ending in `s` (`loads`, `dumps`) operates strictly on Python **S**trings in memory. Methods without `s` (`load`, `dump`) operate directly on **F**ile handles / I/O streams.

- **How it Works:**
  1. `json.load(fp)`: Reads raw JSON data directly from an open file handle `fp` and parses it into native Python objects.
  2. `json.loads(s)`: Takes a JSON-formatted Python string `s` in memory and parses it into native Python objects.
  3. `json.dump(obj, fp, indent=...)`: Takes a native Python object `obj` and serializes it directly into an open file handle `fp`.
  4. `json.dumps(obj, indent=...)`: Takes a native Python object `obj` and returns a formatted JSON `str`.
  5. `indent=2` or `indent=4`: Optional parameter in `dump`/`dumps` that formats the JSON with clean indentation and newlines for human readability.

- **Ari's Code:**
  *JSON Reading, Traversal, and Serialization (`src/01_json_environments_git/practice/json_practice1.py`):*
  ```python
  import json
  from pathlib import Path

  BASE_DIR = Path('.', 'src', '01_json_environments_git')
  USER_PATH = BASE_DIR / 'data' / 'users.json'

  # 1. Loading JSON directly from a file handle
  with open(USER_PATH, 'r') as json_fh:
      users = json.load(json_fh)

  # 2. Navigating nested JSON keys
  for user in users:
      name = user["name"]
      city = user["address"]["city"]
      company_name = user.get("company", {}).get("name")
      print(f"{name} lives in {city} and works at {company_name}.")

  # 3. Serializing a Python dict to a formatted JSON string
  user = users[0]
  formatted_string = json.dumps(user, indent=2)
  print(formatted_string)
  ```

- **Common Pitfalls:**
  1. **Double-Serialization (String treated as value)**: Passing a serialized JSON string to `json.dump(str_data, file)` instead of the native Python dict. Python treats the string as a single scalar value and outputs an escaped string literal with `\"...\"`.
  2. **File Mode Mismatch**: Opening a file with `'r'` (read mode) when attempting to `json.dump()` into it, or omitting `'w'` (write mode).
  3. **Method Confusion (`loads` vs `load`)**: Trying to pass a file pointer to `json.loads(f)` or passing a raw string to `json.load(s)`. Remember: **`s` is for String**.


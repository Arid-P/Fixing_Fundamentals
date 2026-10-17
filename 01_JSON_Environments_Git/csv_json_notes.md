# Milestone 01 Study Notes: CSV ↔ JSON Bridge & Tabular Data Manipulation (M01.13)

## CSV ↔ JSON Bridge & Tabular Data Manipulation
- **The Mental Model:**
  - **Hierarchical Tree vs. Flat Grid**: JSON represents nested trees with rich types (strings, numbers, booleans, null, nested arrays/objects). CSV is a flat 2D spreadsheet table where everything is plain text separated by commas.
  - **The Untyped Nature of CSV**: CSV has no type system. When an integer `1` or a boolean `True` is written to a CSV, it becomes raw text characters. Reading it back yields `"1"` and `"True"`. Converting them back into native Python types (`int()`, `float()`) is strictly the developer's responsibility.
  - **DictReader / DictWriter**: Instead of fragile list-index indexing (`row[0]`, `row[2]`), `DictReader` and `DictWriter` map row values directly to column headers (`row["email"]`), making your code immune to column reordering.

- **How it Works:**
  1. **Flattening Nested Data**: Unpack deep JSON keys (e.g., `user["address"]["city"]`) into a flat, single-level dictionary for tabular export.
  2. **Writing CSV (`DictWriter`)**:
     - Define `fieldnames = [...]`.
     - Open file with `newline=""` and `encoding="utf-8"`.
     - Call `writer.writeheader()` to write column titles.
     - Call `writer.writerows(list_of_dicts)` to write data.
  3. **Reading CSV (`DictReader`)**:
     - Automatically consumes the first line as column header keys.
     - Yields each subsequent line as a `dict[str, str]`.
  4. **Converting Back to JSON**: Pass the list of parsed row dictionaries to `json.dump(rows, file, indent=2)`.

- **Ari's Code:**
  *JSON to CSV and CSV to JSON Bridge (`src/01_json_environments_git/practice/csv_manuplication.py`):*
  ```python
  from pathlib import Path
  from csv import DictReader, DictWriter
  from json import load, dump

  BASE_DIR = Path('.', 'src', '01_json_environments_git')
  USER_JSON_PATH = BASE_DIR / 'data' / 'users.json'
  USER_CSV_PATH = BASE_DIR / 'data' / 'users.csv'
  OUTPUT_PATH = BASE_DIR / 'data' / 'users_from_csv.json'

  # 1. Load original JSON
  with open(USER_JSON_PATH, 'r', encoding='utf-8') as file:
      users = load(file)

  # 2. Flatten hierarchical JSON into 1D rows
  data = []
  keys = ['id', 'name', 'email', 'city']
  for user in users:
      data.append({
          "id": user["id"],
          "name": user["name"],
          "email": user["email"],
          "city": user["address"]["city"]
      })

  # 3. Write rows to CSV
  with open(USER_CSV_PATH, 'w', newline='', encoding='utf-8') as file:
      writer = DictWriter(file, fieldnames=keys)
      writer.writeheader()
      writer.writerows(data)

  # 4. Read CSV and dump back to JSON
  with open(USER_CSV_PATH, 'r', encoding='utf-8') as file:
      rows = list(DictReader(file))

  with open(OUTPUT_PATH, 'w', encoding='utf-8') as file:
      dump(rows, file, indent=2)
  ```

- **Common Pitfalls:**
  1. **Omitting `newline=""` in `open()`**: Omitting this parameter causes Python's default writer and specific operating systems (like Windows) to inject extra `\r` carriage returns, resulting in blank empty rows between data records.
  2. **Type Assumption Bugs**: Expecting numbers from `DictReader`. Evaluating `if row["id"] == 1:` will always evaluate to `False` because `row["id"]` is the string `"1"`.
  3. **Forgetting `writeheader()`**: Calling `writer.writerows()` without calling `writer.writeheader()` first produces a CSV without column names, which breaks downstream `DictReader` consumers.


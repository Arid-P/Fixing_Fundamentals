"""
Milestone 01 Final Build Deliverable: Todo CLI Tool (todo_tool.py)

OVERVIEW:
Build a command-line interface (CLI) using Python's built-in `argparse` module 
to interact with and manage `todos.json` and `users.json`.

COMMAND SPECIFICATIONS:

1. `list --user <ID>`
   - Shows all todos belonging to the specified user ID.
   - Output format: Clean list or table showing status and title.
     e.g.:
       [✓] Clean room
       [ ] Read book
   - If the user has no todos or doesn't exist, show a helpful message.

2. `stats`
   - Prints a clean summary table showing statistics for every user:
     User Name | Total Tasks | Completed Tasks | Incomplete Tasks
   - Cross-references user names from `users.json` with tasks from `todos.json`.

3. `add --user <ID> --title "<TITLE>"`
   - Creates a new todo item:
     - `userId`: specified integer
     - `id`: max existing todo id + 1 (dynamic, not hardcoded)
     - `title`: specified title string
     - `completed`: False
   - Appends it to the todos list.
   - Saves safely using the Atomic Write Pattern:
     * Check if target file exists; if so, create a backup copy (`todos.json.bak`).
     * Write new data to a temporary file (`todos.json.tmp`) with indent=2, encoding="utf-8".
     * Atomically swap using `os.replace(temp_file, target_file)`.
   - Prints a success confirmation with the new todo ID.

DEFENSIVE ERROR HANDLING:
- If `todos.json` contains invalid JSON syntax, catch `json.JSONDecodeError` 
  and print a friendly message (line, column, error reason) instead of crashing with a traceback.
- If data files are missing, handle `FileNotFoundError` gracefully.

ACCEPTANCE CRITERIA:
- Running `python todo_tool.py --help` shows usage for list, stats, and add.
- Adding a todo updates the file and creates/updates a `.bak` file.
- Running `stats` displays consistent totals before and after adds.
"""

from pathlib import Path
from os import replace
from shutil import copy

from json import load, dump, JSONDecodeError
import argparse

from icecream import ic #To debug
ic.disable()

#0. Creating the parser and subparsers to read the arguments from the command line.

parser = argparse.ArgumentParser(description="My Task Manager")
subparsers = parser.add_subparsers(dest="command", required=True)

list_parser = subparsers.add_parser("list", help="List todos for a user")
list_parser.add_argument("--user", type=int, required=True, help="User ID number")

stats_parser = subparsers.add_parser("stats", help="Prints a clean summary table showing statistics for every user")

add_parser = subparsers.add_parser("add", help="Create a neww todo and then adds it into the todo list")
add_parser.add_argument("--user", type=int, required=True, help="User ID number")
add_parser.add_argument("--title", type=str, required=True, help="The title of the new todo")

args = parser.parse_args()


#1. Specificing paths
DATA_DIR = Path(__file__).parent.parent / 'data'
USER_DIR = DATA_DIR / 'users.json'
TODO_PATH = DATA_DIR / 'todos.json'

users, todos = [], []

#2. Loading the data
def load_data () -> None:
    global users, todos

    try: 
        with open(USER_DIR, 'r') as file:
            try:
                users = load(file)
            except JSONDecodeError as e:
                    print("Unable to process users.json as the json is not in proper format.")
                    exit()

        with open(TODO_PATH, 'r') as file:
            try:
                todos = load(file)
            except JSONDecodeError as e:
                    print("Unable to process todos.json as the json is not in proper format.")
                    exit()
        
    except FileNotFoundError as e:
            if 'user' in e.filename:
                print('users.json ', end='')
            else:
                print('todos.json ', end='')
    
            print("file not found")
            exit()


def list_user_todo (userid: int) -> None:
    global todo
    todo_of_user = list(filter(lambda todo: todo.get('userId') == userid, todos ))

    if not todo_of_user:
        print("No todo found for the provided user.")
        return 

    print(f"{'Title':^70} | {'Status':^6}|")
    print("-" *90)

    for todo in todo_of_user:
        title = todo.get('title') or "No title found"
        status = '[✓]' if todo.get('completed') else '[ ]'

        print(f"{title:<70} | {status:^6}|")
    print("-" * 90)


def display_stats () -> None:
    global users, todos

    #Initialse a hashmap to count total tasks, completed and incompleted for every userId
    user_task_details: dict[int, list[int, int, int, str]] = {
        user.get('id'): [(user.get('name') or 'No username found'), 0, 0, 0]
        for user in users
    } 

    #Count total, completed and, incompleted for every user
    for todo in todos:
        id = todo.get('userId')
        user_task_details[id][1] += 1

        if todo.get('completed'):
            user_task_details[id][2] += 1
        else:
            user_task_details[id][3] += 1

    print(f"{'Name':<25} | {'Total':^5} | {'Completed':^8} | {'Pending':^7} |")
    print('-'*90)

    for details in user_task_details.values():
        name, total, completed, pending = details[0], details[1], details[2], details[3]

        print(f"{name:<25} | {total:^5} | {completed:^8} | {pending:^7} |")
    print('-'*90)


def write_todos_safely(data, target_file_path: Path=TODO_PATH) -> None:
    BACKUP_FILE = target_file_path.parent / f'{target_file_path.name}.bak'
    TEMP_FILE = target_file_path.parent / f'{target_file_path.name}.tmp'

    #creating the directories    
    target_file_path.parent.mkdir(parents=True, exist_ok=True)

    #To make sure the file exists
    if target_file_path.exists():
        copy(target_file_path, BACKUP_FILE)    

    #writing to temp
    with open(TEMP_FILE, 'w') as file:
        dump(data, file, indent=4, default=str)

    replace(TEMP_FILE, target_file_path) 


def add_todo (userId: int, title: str) -> None:
    global users, todos

    #Finding the new id for the todo
    max_todo_id = 0
    for todo in todos:
        max_todo_id = max(max_todo_id, todo.get('id'))
    
    todo = {
        'userId' : userId,
        'id' : max_todo_id+1,
        'title' : title,
        'completed' : False
    }

    todos.append(todo)

    write_todos_safely(todos)
    print(f"Successfully added todo #{todo['id']}: '{title}' for user {userId}")




load_data()

if args.command == "list":
    ic("list")
    list_user_todo(args.user)
elif args.command == "stats":
    ic("stats")
    display_stats()
else:
    ic("adding")
    add_todo(args.user, args.title)


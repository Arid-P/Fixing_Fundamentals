"""
TODO:
Requirements for the build:

- Load Data: Done
    Read and parse both users.json and odos.json.

- Aggregate & Display: Done
    For every user, calculate: total todos, completed count, pending count.
    Print a clean summary report to the terminal.

- Mutate:
    Append a new todo item for user ID 1 (e.g., {"userId": 1, "id": 201, "title": "Master JSON and Git merge conflicts", "completed": True}).

- Persist:
    Write the updated todos list into src/01_json_environments_git/data/updated_todos.json with indent=2.
"""

from json import load, dump
from pathlib import Path

#0. Specificing paths and constants
DATA_DIR = Path(__file__).parent.parent / 'data'
USER_DIR = DATA_DIR / 'users.json'
TODO_PATH = DATA_DIR / 'todos.json'
UPDATE_TODO_PATH = DATA_DIR / 'updated_todo.json'

max_todo_id = 0

#1. Loading the data 
with open(USER_DIR, 'r') as file:
    users = load(file)

with open(TODO_PATH, 'r') as file:
    todos = load(file)


#2. Aggregating it
user_task_details: dict[int, list[int, int, int]] = {} 
#{user_id: [completed, pending, total]}

for user in users:
    user_task_details[user.get('id')] = [0, 0, 0]

for todo in todos:
    id = todo.get('userId')
    user_task_details[id][2] += 1

    if todo.get('completed'):
        user_task_details[id][0] += 1
    else:
        user_task_details[id][1] += 1

    max_todo_id = max(max_todo_id, todo.get('id'))
    


#3. Displaying the data
print(f"{'User':^25} | {'Total':^8} | {'Completed':^8} | {'Pending':^8}|")
print("-" * 65)

encountered = []
for user in users:
    id = user.get('id')

    if id in encountered:
        continue
    else:
        encountered.append(id)

    name = user.get('name')
    todo = user_task_details[id]

    print(f"{name:<25} | {todo[2]:>8} | {todo[0]:>8} | {todo[1]:>8} |")
print("-" * 65)


#4. New todo
userID = int(input("Enter the user's id: "))
title = input("Enter the todo title: ")
todo_id = max_todo_id + 1

todo = {
    'userId' : userID,
    'id' : todo_id,
    'title' : title,
    'completed' : False
}

todos.append(todo)

with open(UPDATE_TODO_PATH, 'w') as file:
    dump(todos, file, indent=4)
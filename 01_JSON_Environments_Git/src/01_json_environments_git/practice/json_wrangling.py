from json import load
from pathlib import Path
from collections import Counter, defaultdict

#to debug
from icecream import ic

BASE_DIR = Path(__file__).parent.parent
USERS_PATH = BASE_DIR / 'data' / 'users.json'
TODOS_PATH = BASE_DIR / 'data' / 'todos.json'


#Loading users.json and todos.json
with open(USERS_PATH, 'r', encoding='utf-8') as file:
    users = load(file)

with open(TODOS_PATH, 'r', encoding='utf-8') as file:
    todos = load(file)

#TASK_1
todo_titles_uid1 = [el.get('title') for el in list(filter(lambda todo: todo.get('userId') == 1 and todo.get('completed'), todos)) ]

#Task_2
todos_count = Counter(todo.get('completed') for todo in todos)
print(f"Number of completed TODO's = {todos_count[True]}\nNumber of incomplete TODO's = {todos_count[False]}")

#Task_3
grouped_todo = defaultdict(list)
for todo in todos:
    if todo.get('completed'):
        grouped_todo[todo.get('userId')].append(todo)

l_grouped_todo = sorted(grouped_todo.items(), key=lambda t: -1 * len(t[1]) )
#you can also do
#[t.get('title') for t in todos if t.get('userId') == 1 and t.get('completed')]
sorted_todo = {el[0]: el[1] for el in l_grouped_todo} 

print(sorted_todo)
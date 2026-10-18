# Milestone 01: JSON and Git Merge Conflicts.

## Goal

1. What is JSON, how we read and understand it. 
2. How we handle JSON files, extracting data, writting data, and other operations, using python.
3. Under standing merging, the different  conflicts which can arise, methods to resolve these conflicts and some advanced git. 

## What I built
- **`process_todos.py`:** It takes the users and todos from `users.json`, `todos.js`respectively and aggregates the todo which each user has and displays it. It also gives you the option to add a new todo.

- **`todo_tool.py`:** It manages users.json and todos.json by passing command linbe agruments upon running of the python script.

## What actually clicked
### 1. JSON

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

_***Use of JSON Along with CSV***_
- **`csv.DictReader(<file>)`:** It reads the content of a csv file. It returns a *csv object* so converting to a list using `list()` is important. For example

- **`csv.DictWriter(<file>, fieldnames=<List of the keys, newline='', encoding='utf-8')`:** It writes content to a csv file. It is __*done in 3 parts*__. It is best practice to provide `newline=''` and `encoding='utf-8`. 
    A common example for both is given below:
    ```python
    import csv

    # Reading CSV into a list of dicts:
    with open("data.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)  # list of dicts!

    # Writing list of dicts to CSV:
    with open("data.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "city"])
        writer.writeheader()
        writer.writerows(rows)
    ```

## 2. GIT

- **`git fetch`:** It downloads all the new commits, branches, and tags into your local .git repo from the remote server. They are download in a separate branch (e.g., origin/main). *No working File is Ever Touched*. 

- **`git pull`:** It is `git fetch` and `git merge` at once, i.e., it downloads all the new elements (commits, branches, etc) from the remote servers in a separate brnch and then merges it with the local branch(es).
        $$git pull = git fetch + git merge$$

- **Merge Conflict:** It occurs only if two or more users edit the same line(s). Git represents conflicts in a specific format, *HEAD* : Marks the start of your current branch's version; *==== The divided line*: The divider line. Everything above is your local version; everything below is the incoming version; *<branch_or_commit>*: Marks the end of the incoming branch's version. For example:
    ```git
    <<<<<<< HEAD
    print("Welcome to Todo CLI v1.0 (local edit)")
    =======
    print("Welcome to Todo CLI v2.0 (incoming from remote)")
    >>>>>>> feature-branch
    ```
    Decide what the code should be: keep your version, keep their version, or combine them both. Then delete all the marker lines, and stage all the edits. 

- **`3 Git Areas`:** Git has 3 different areas or section where files can exist. The first is *Working Directory* it is simply the directory and its contents that you see. In it you create, edit, read, delete files. 
    Then we have *Staging area*, here you add or stage the files to be commited. Say you edit 5 files, but want only 3 to be commit then you add those there to the stage area and commit them. We done update any file here, on running `git add`, git takes a snapahot of the working directory and saves it. "That is what "staged" means: *marked and prepared to be included in the next commit*.*". 
    Then you have the *Repositry* or common refered to as repo. When you run `git commit`, Git seals the packing box, gives it a unique cryptographic ID (SHA hash), and stores it permanently in the `.git` directory as a snapshot. The staging area is now clean and ready for the next round.

- **`git switch ~-c~ <branch-name>`:** It is the new way to switch to a branch. The `-c` flag creates the branch if it doesnt already exist.

- **`git branch`:** Lists all local branches, with an asterisk `*` next to the one you are currently standing on.

- **`git branch -d/-D <branch-name>`:** It is used to delete a branch. The `-d` and `-D` are safe and forced flags (not exactly that but for understanding). The `-d` gives you an error message if the branch you are trying to delete hasnt been merged with your current branch or upstream, telling you that and saying to merge. While `-D` straight up deletes the branch without any messaeg or shit. 

- **`Fast-Forward vs. Three-Way Merge`:** Fast forward occurs when there have been no commits after the commit you branched from, ie, the graph looks like 2 line segements with a common vertex.
    ```text
    Before Merge:
    A --- B --- C (main)
                \
                D (temp-test)

    After Fast-Forward Merge:
    A --- B --- C --- D (main, temp-test)
    ```
    Three way merge occurs when the there are more commits from the commit you branched off. It is best understood by a visual:
    ```text
    Before Merge:
    A --- B --- C (Common Ancestor)
                \
                \--- E (main)
                \-- D (feature-banner)

    After Three-Way Merge:
    A --- B --- C ------- E ---- M (Merge Commit - 2 parents!)
                \              /
                \--- D ------/
    ```

- **`git remote -v`:** A "remote" is an alias stored in the `.git/config` that points to a URL. By convention, git names your primary remote __`origin`__. The `-v` stands for verbose. It shows all the configured remotes with thier alias and URL.

- **`git remote add <alias> <url>`:** It adds/configures a remote with its alias and URL. Eg:
    ```bash
    git remote add origin https://github.com/your-username/your-repo.git
    ```
    In open-source work, you often have origin pointing to your fork, and you add a second remote called upstream pointing to the original author's repository

- **`git push -u origin <branch>`:** The `-u` is short for `--set-upstream`. It creates a permanent tracking link between your local branch (main) and the remote branch (origin/main). Once you have set it up and want to push the changes you can simply do `git push`.  

- **`git clone <url>`:** It simply clones the git repo into your system as a directory. It downloads the whole history and everything (the `.git` folder). 

- **`git diff`:** It shows the un-staged changes. Simply answers the question *"What have I edited on my workbench that I haven't staged yet?"*

- **`git diff --staged`:** It tells you what all will be commit in your next commit. Answering the question *"What is packed inside my staging box right now, waiting to be committed?"*

- **`git diff origin/main`:** It shows all the code changes __across the commits__ you __havent pushed__ yet. Answering *"What code exists on my computer that is NOT yet on GitHub?"*

- **`git log`:** It gives you the commit history in chronological order (recently first) of the branch you currently on. It has several flags: `--all`, it gives a complete view of where your local branch is relative to the remote server; `--graph`, it displays the commit history in somewhat graph manner in the command line; `--oneline`, it presents each commit with its hash and the message in a line. 

- **`.gitignore`:** Inside iy you define the directories and folder that git needs to ignore. eg `*.log` tells every file ending with `.log`, `.venv/` tells Git to ignore this entire directory, `temp/*`, tells git to ignores all files inside the temp/ folder, `!keep_me.log` (An exclamation mark is a negation rule) tells git to not ignore this specific file, even if *.log matched earlier.
    __*Note:*__ It tells git to not start tracking a file! Already tracked files have no effect on them.

- **`git rm --cached <file-name/directory>`:** It removed a file or directory from git's tracking. `--cached` preserves that file on your disk, without it the file is deleted form boht git and disk.

- **``:**

- **``:**

- **``:**

- **``:**

- **``:**

- **``:**

- **``:**

- **``:**

- **``:**

- **``:**


## What I struggled with
- json.dumps. Now it is ok.

## Open questions / revisit later
None
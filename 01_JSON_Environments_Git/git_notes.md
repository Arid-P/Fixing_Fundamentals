# Milestone 01 Study Notes: Git Deep Dive & Conflict Mastery (M01.14 – M01.24)

---

## 1. The Three Git Areas & What "Staged" Means (M01.14)
- **The Mental Model:**
  - **Working Directory (The Workbench)**: The actual files on your physical hard drive that you see and edit in your code editor. Edits here exist only in your local workspace.
  - **Staging Area / Index (The Packing Box)**: A preparatory loading dock. You don't have to ship all workbench edits at once. Running `git add` takes a snapshot of specific files and packs them into the box. "Staged" means *marked and packed, ready to be sealed into the next snapshot*.
  - **Repository (.git Vault)**: The permanent, immutable database of snapshots. Running `git commit` permanently seals the packing box, generates a unique cryptographic SHA hash, and records it in history.

- **How it Works:**
  ```text
  [Working Directory]  ----(git add)---->  [Staging Area]  ----(git commit)---->  [Repository (.git)]
    (Unstaged/Red)                            (Staged/Green)                          (Committed Vault)
  ```
  1. `git status`: Checks the state of all three areas (shows unstaged files in red, staged files in green).
  2. `git add <path>`: Moves changes from the Working Directory into the Staging Area.
  3. `git commit -m "..."`: Converts the current Staging Area into a permanent commit in the Repository.

- **Ari's Terminal Evidence:**
  ```bash
  # Unstaged state (Working Directory):
  # Changes not staged for commit:
  #   modified:   01_JSON_Environments_Git/README.md

  # Staged state (Staging Area):
  # Changes to be committed:
  #   modified:   01_JSON_Environments_Git/src/01_json_environments_git/data/todos.json
  ```

- **Common Pitfalls:**
  - Assuming saving a file in VS Code commits it to Git. Saving only touches the Working Directory.
  - Running `git commit` before running `git add`, resulting in `no changes added to commit`.

---

## 2. Branch Lifecycle & Deletion Safety (M01.15)
- **The Mental Model:**
  - In Git, a branch is **not** a duplicate folder of your codebase. A branch is a lightweight **41-byte movable pointer** (like a sticky note) pointing to a specific commit.
  - The special pointer **`HEAD`** indicates which branch sticky-note you are currently standing on.

- **How it Works:**
  1. `git switch -c <name>`: Atomically creates a new branch pointer AND switches your `HEAD` to it.
  2. `git switch <existing>`: Moves `HEAD` between existing branches (updates your working directory files to match that branch's snapshot).
  3. `git branch`: Lists all local branches; `*` indicates current `HEAD`.
  4. `git branch -d <name>` (Safe Delete): Deletes a branch **only** if all its commits are fully merged into `HEAD`. If unmerged work exists, Git refuses to delete it to prevent data loss.
  5. `git branch -D <name>` (Force Delete): Permanently destroys the branch pointer, even if commits are unmerged and orphaned.

- **Ari's Terminal Evidence:**
  ```bash
  # Git's built-in safety net blocking unmerged branch deletion:
  $ git branch -d temp-test
  error: the branch 'temp-test' is not fully merged
  hint: If you are sure you want to delete it, run 'git branch -D temp-test'

  # Safe deletion after merging:
  $ git merge temp-test
  $ git branch -d temp-test
  Deleted branch temp-test (was 6213621).
  ```

- **Common Pitfalls:**
  - Using `git branch -D` carelessly and permanently losing days of unmerged work. Always start with lowercase `-d`.

---

## 3. Merge Types: Fast-Forward vs. Three-Way Merge (M01.16, M01.17, M01.18)
- **The Mental Model:**
  - **Fast-Forward Merge (Straight Line)**: Happens when the target branch (`main`) has had **zero** new commits since the feature branch split off. Git simply slides the `main` pointer forward. No merge commit is created; `git log --graph` remains a single linear line.
  - **Three-Way Merge (True Merge / Diverged History)**: Happens when both `main` and the feature branch have moved forward independently since their Common Ancestor. Git compares three snapshots (Common Ancestor, HEAD, and incoming branch) and creates a new **Merge Commit** with two parents.
  - **Merge Conflict**: Occurs during a three-way merge when both branches modified the exact same line(s) since the Common Ancestor. Git pauses and writes conflict markers.

- **How it Works:**
  1. Decode markers:
     ```text
     <<<<<<< HEAD
     (Code on your current branch)
     =======
     (Code on the incoming branch)
     >>>>>>> branch-name
     ```
  2. Resolution workflow:
     - Open file, choose desired code, and **delete all marker lines**.
     - Stage resolved file: `git add <file>`.
     - Complete merge: `git commit` (or `git merge --continue`).
     - Bail out if needed: `git merge --abort`.

- **Ari's History Graph Evidence:**
  ```text
  # Fast-Forward Merge (Straight linear progression):
  * 6213621 (HEAD -> main) feat(test): add dummy feature
  * 85b8cae chore(vscode, README.md): configure python environment...

  # Three-Way Merge with Resolved Conflict (Visible fork and reunion):
  *   7781706 Merge branch 'feature-banner'
  |\  
  | * 25139f2 feat(banner): update banner on feature branch
  * | 734e523 feat(banner): update banner on main branch
  |/  
  * aa3e0be feat(cli): initialize todo_tool with banner
  ```

- **Common Pitfalls:**
  - Leaving conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) inside the code when committing, causing syntax errors in production.
  - Panicking during a conflict instead of using `git merge --abort` to return to a clean pre-merge state.

---

## 4. Remotes Beyond Fetch & Pull (M01.19, M01.20)
- **The Mental Model:**
  - A "remote" is simply an alias nickname pointing to a remote URL (default is `origin`).
  - **`git fetch` vs `git pull`**:
    $$\text{git pull} = \text{git fetch} + \text{git merge}$$
    - `git fetch`: Safely downloads all new commits from GitHub into remote-tracking branches (`origin/main`). **Never touches your working files.**
    - `git pull`: Downloads via fetch AND immediately forces a merge into your active branch.
  - **`git clone`**: Does not just copy files—it clones the entire historical `.git` database, configures `origin`, and checks out the default branch.
  - **`-u` (`--set-upstream`)**: Binds your local branch to a remote branch so future commands only require typing `git push` or `git pull`.

- **How it Works:**
  1. `git remote -v`: Lists all remote aliases and URLs.
  2. `git remote add <name> <url>`: Registers a new remote.
  3. `git push -u origin <branch>`: Pushes commits and sets tracking.

- **Ari's Terminal Evidence:**
  ```bash
  $ git remote -v
  origin  https://github.com/Arid-P/Fixing_Fundamentals.git (fetch)
  origin  https://github.com/Arid-P/Fixing_Fundamentals.git (push)
  ```

- **Common Pitfalls:**
  - Blindly running `git pull` when you have unstaged local work, causing sudden merge conflicts. Use `git fetch` first to inspect incoming changes safely.

---

## 5. History & Diff Inspection (M01.21)
- **The Mental Model:**
  - Inspecting code requires looking across specific boundaries:
    1. Working Directory vs. Staging Area (`git diff`)
    2. Staging Area vs. Last Commit (`git diff --staged`)
    3. Local Machine vs. GitHub Remote (`git diff origin/main`)
    4. Complete Multi-Branch Panoramic View (`git log --oneline --graph --all`)

- **How it Works:**
  1. `git diff`: Shows unstaged edits on your workbench.
  2. `git diff --staged`: Shows what will be included in the next commit.
  3. `git diff origin/main`: Shows everything committed locally that hasn't been pushed to GitHub yet.
  4. `git log --oneline --graph --all`: Renders the complete ASCII branch tree across all local and remote branches.

- **Common Pitfalls:**
  - Running `git diff` after running `git add` and thinking your changes disappeared because the output is empty. Remember: once staged, use `git diff --staged`!

---

## 6. `.gitignore` & The Already-Tracked Trap (`git rm --cached`) (M01.22)
- **The Mental Model:**
  - `.gitignore` only prevents **untracked** files from being added to Git.
  - **The Trap**: If a file was already committed in the past, adding it to `.gitignore` does **nothing**. Git will continue tracking its changes indefinitely.
  - **The Escape Hatch (`git rm --cached`)**: Removes the file from Git's tracking/staging area (the index) while leaving the physical file completely untouched on your hard drive.

- **How it Works:**
  1. Delete from tracking only: `git rm --cached <file>` (or `git rm -r --cached <folder>`).
  2. Add the path/pattern to `.gitignore`.
  3. Commit the deletion: `git commit -m "chore: untrack <file>"`.

- **Ari's Terminal Evidence:**
  ```bash
  $ git rm -r --cached .vscode
  rm '.vscode/settings.json'
  $ git commit -m "chore(settings.json): removed .vscode/settings.json from tracking..."
  # .vscode/settings.json remains on disk, but Git no longer tracks it!
  ```

- **Common Pitfalls:**
  - Running `git rm <file>` without `--cached`, which deletes your actual file off the hard drive! Always use `--cached` when you want to keep the local file.

---

## 7. The Git Undo Toolkit (`restore`, `reset`, `revert`) (M01.23)
- **The Mental Model:**
  - The decision rule based on where the mistake lives:
    - **Mistake on Workbench (Uncommitted)**: $\rightarrow$ `git restore`
    - **Mistake in Local Commit (Not Pushed)**: $\rightarrow$ `git reset`
    - **Mistake Already Pushed to GitHub**: $\rightarrow$ `git revert`

- **How it Works:**
  1. `git restore <file>`: Discards unstaged modifications in working directory.
  2. `git restore --staged <file>`: Unstages files without losing edits.
  3. `git reset --soft HEAD~1`: Undoes commit; leaves all files staged in green.
  4. `git reset --mixed HEAD~1` (default): Undoes commit; moves files to unstaged red.
  5. `git reset --hard HEAD~1` (Nuclear): Undoes commit and permanently wipes out all changes.
  6. `git revert <commit-hash>`: Creates a **new inverse commit** that cancels out the bad commit without rewriting public history.

- **Ari's Terminal Evidence:**
  ```bash
  # Safe public revert preserving history:
  $ git revert HEAD --no-edit
  $ git log --oneline -n 2
  3a54436 (HEAD -> main) Revert "feat(temp): add breaking change"
  cf30f00 (origin/main) feat(temp): add breaking change
  ```

- **Common Pitfalls:**
  - Running `git reset --hard` on commits that were already pushed to GitHub. This rewrites history and breaks collaborators' repositories. Always use `git revert` for pushed commits.

---

## 8. Conventional Commits Hygiene (M01.24)
- **The Mental Model:**
  - Commit logs are not diary entries; they are an automated changelog for teams.
  - Follows: `<type>(<scope>): <imperative summary>`
  - Types: `feat` (new feature), `fix` (bug fix), `refactor` (code reorganization), `docs` (documentation), `test` (tests), `chore` (maintenance/config).
  - The Imperative Mood Test: *"If applied, this commit will [your message]."* Always use present tense ("add", "fix", "refactor", never "added" or "fixed").
  - Optional Body: Separate by a blank line to provide detailed rationale, bullet points, and context.

- **Examples:**
  ```text
  # Good:
  feat(cli): implement interactive task manager CLI for users and todos
  fix(cli): resolve duplicate todo ID generation and empty user display

  # With body context:
  fix(cli): resolve duplicate todo ID generation and empty user display

  - Increment max_todo_id by 1 to ensure unique task identifiers
  - Add early return with helpful message when user has zero tasks
  - Gracefully terminate on JSONDecodeError to protect file integrity
  ```


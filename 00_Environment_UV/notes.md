# Milestone 00 Study Notes: Modern Python Tooling with `uv`

## Modern Python Tooling & Dependency Management with uv
- **The Mental Model:**
  - **`pyproject.toml` vs `uv.lock`**: `pyproject.toml` is your grocery shopping list (what ingredients you want: "milk, apples"). `uv.lock` is the itemized register receipt with exact brand, barcode, batch number, and cryptographic checksum. You write the grocery list; `uv` writes the receipt.
  - **`uv lock` vs `uv sync`**: `uv lock` is the architect drawing the blueprint on paper (pure math/graph resolution, no construction). `uv sync` is the construction crew actually pouring concrete and building `.venv` to match the blueprint.
  - **`uv run`**: A chauffeur who instantly sets up the right environment in the background, drives you to your destination, and leaves zero mess in your terminal shell. Manual venv activation (`source .venv/bin/activate`) is obsolete.
  - **PEP 723 (`uv add --script`)**: A self-contained backpack for a single script. The script carries its own dependencies in a comment header so you don't need a whole suitcase (project folder, `.venv`, `pyproject.toml`) for a quick trip.

- **How it Works:**
  1. `uv init`: Generates `pyproject.toml` (project manifest) and `.python-version` (pinned runtime version).
  2. `uv add <pkg>`: Auto-creates `.venv` if absent, resolves the full transitive dependency graph, updates `pyproject.toml`, and creates/updates `uv.lock`.
  3. `uv run <script.py>`: Locates the project root, verifies `.venv` matches `uv.lock` (auto-syncing if out of date), injects the environment ephemerally, and executes the script.
  4. `uv remove <pkg>`: Purges the package from `pyproject.toml`, recalculates `uv.lock`, and removes wheels from `.venv`.
  5. `uv lock --upgrade`: Re-resolves `uv.lock` against the latest allowable versions without touching your code.
  6. `uv sync`: Forces `.venv` to match `uv.lock` exactly, cleaning up stale packages and installing missing ones.
  7. `uv add --script <file.py> <pkg>`: Injects a PEP 723 metadata comment header directly into a standalone `.py` file, runnable via `uv run <file.py>`.
  8. `uv python install <ver>` & `uv python pin <ver>`: Installs isolated CPython standalone binaries directly without root or `pyenv`, and pins the local directory's version.

- **Ari's Code:**
  *Standalone PEP 723 Script (`src/00_environment_uv/practice/inline_demo.py`):*
  ```python
  # /// script
  # requires-python = ">=3.14"
  # dependencies = [
  #     "rich>=15.0.0",
  # ]
  # ///
  from rich import print

  print("[bold green]PEP 723 Inline Script is working![/bold green]")
  ```

- **Common Pitfalls:**
  1. **Standard Library Confusion**: Modules like `os`, `sys`, `random`, `math`, `json`, and `datetime` are built into Python. Running `uv add datetime` installs an unrelated legacy third-party package from PyPI that is shadowed and unnecessary. Only use `uv add` for external packages.
  2. **Editing `uv.lock` by Hand**: Never touch `uv.lock` manually. If you want to change dependencies, edit `pyproject.toml` or use `uv add`/`uv remove`, then let `uv` update the lockfile.
  3. **Manually Activating Environments**: Running `source .venv/bin/activate` is unnecessary and introduces state leakage across terminal tabs. Always execute with `uv run`.

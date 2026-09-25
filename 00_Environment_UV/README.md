# Milestone 0X: <name>

## Goal
- Learing uv, how to use it. What it actually does under the hood and how it is more efficent than venv

- **`game.py`and `calc.py`:** Some old file that I will use for examples. 


## What I built
An understanding of how uv is initialised, and manages pacakages.

## What actually clicked
- **`uv init`:** What it actually does. It creates `.python_version`, `pyproject.toml` which store the critical information regardign the project, the python version, dependencies.

- **`uv add`:** It added the specified pakages along with thier prerequisites. It also creates the `/.venv` directory, `uv.lock `file. The creation of the directory and file is automatic, no intervention required from the user.

- **`pyproject.toml` v/s `uv.lock`:** toml store the dependency and its minimum (or exact) version. But on running `uv sync` on some other machine, it make install a newer version of some library which may not be compatiable. Hence uv uses `uv.lock`, it saves the exact version, links, commands, and the information for every dependency so that on `uv sync` that exact snap is insatleld and evrything works prefectly. 

- **`uv run`:** It runs the python file using the enviroment in the current directory automatically without the user needing to define it. It also doesnt chaneg your terminal' shell state unlike thye old venv commands. Most important, if it finds any discrepancies within the dependencies then it automatically syncs them using `uv sync`.

## What I struggled with
For now none.

## Open questions / revisit later
For now none.


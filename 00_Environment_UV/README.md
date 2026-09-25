# Milestone 00: Environment & Tooling (uv)

## Goal
- Learing uv, how to use it. What it actually does under the hood and how it is more efficent than venv

- **`game.py`and `calc.py`:** Some old file that I will use for examples. 


## What I built
An understanding of how uv is initialised, and manages pacakages.

## What actually clicked
- **`uv init`:** What it actually does. It creates `.python_version`, `pyproject.toml` which store the critical information regardign the project, the python version, dependencies.

- **`uv add`:** It added the specified pakages along with thier prerequisites. It also creates the `/.venv` directory, `uv.lock `file. The creation of the directory and file is automatic, no intervention required from the user.

- **`pyproject.toml` v/s `uv.lock`:** toml store the dependency and its minimum (or exact) version. But on running `uv sync` on some other machine, it make install a newer version of some library which may not be compatiable. Hence uv uses `uv.lock`, it saves the exact version, links, commands, and the information for every dependency so that on `uv sync` that exact snap is insatleld and evrything works prefectly. 

- **`uv run`:** It runs the python file using the enviroment in the current directory automatically without the user needing to define it. It also doesnt chaneg your terminal' shell state unlike thye old venv commands. Most important, if it finds any discrepancies within the dependencies then it automatically syncs them using `uv sync`. It also gives the error output fantastically, very neatly organized.**

- **`uv remove`:** As the name suggests it remove any installed dependency. It automatically edits the `uv.lock` and `pyproject.tomal` with the appropriate information.

- **`uv sync`:** It sync the `/.venv` with `uv.lock`. Useful in multiple people working on same software.

- **`uv lock`:** It updates the `uv.lock` without actually installing any libraries or dependencies. It update the blueprint with the necessary information. `uv sync` updates as well as install dependencies. It is most useful when you want to update the blueprint to the latest version or you editted `pyproject.toml` by hand.

- **`uv add --script <file_name>.py <dependencies>`:** When you have to create a throwaway script without managing the whole folder shit. It adds the `pyproject.toml` and `.python_version` details with the file itself, like:
    ```python
    # /// script
    # requires-python = ">=3.12"
    # dependencies = [
    #     "rich",
    # ]
    # ///
    ```
    then you can simply run the file using `uv run <file_name>.py` and uv creates an isolated cache environemnt to run the file and then automatically delets it as well.

- **`uv python <option>`:** Using uv yuo also manage `pyenv` and system python version manager. 
    To check the installed version: 
    ```bash
    uv python list
    ```
    and  to install some exact version
    ```bash
    uv python install 3.12
    ```
    it installs the version in `~/.local/share/uv/python/` for eash access
    You can also pin a python version for a directory like
    ```bash
    uv python pin 3.12
    ```

## What I struggled with
- `uv lock`, didnt understnad why it existed and was used for eactly. But now I do understand it as one simply creates the required blueprint while the other creates as well as applies that blueprint.


## Open questions / revisit later
None.


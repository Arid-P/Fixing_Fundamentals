import logging
import argparse
from pathlib import Path
from typing import Any
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from utilis import get_logger
from utilis import TaskType, int_valid, path_valid

logger: logging.Logger = get_logger(__name__)
console = Console()


# Input fucntions
def _parsering_cli_input() -> argparse.Namespace:
    logger.debug("Establishing CLI parser")

    parser = argparse.ArgumentParser(description="Github Activity Report")

    group: argparse._MutuallyExclusiveGroup = parser.add_mutually_exclusive_group()

    group.add_argument(
        "-i",
        "-I",
        "--info",
        type=str,
        dest="user",
        help="The username of the user whose repo are to be viewed",
    )

    group.add_argument(
        "-t",
        "-T",
        "--token",
        type=str,
        dest="token_path",
        help="The path to the env file",
    )

    parser.add_argument(
        "-n",
        "-N",
        type=int,
        dest="recent_count",
        required=False,
        help="The number of recent repos to be viewed",
    )

    args: argparse.Namespace = parser.parse_args()
    logger.info("Parser created successfully")
    logger.debug("Parsed arguments: %s", args)

    return args


def _prompt_input() -> dict[str, TaskType | str | int | Path]:
    logger.info("Prompting the user for input.")

    print("1. Information regarding a user\n2. Enter Github Token\n3. Exit")

    logger.info("Validating the task number chosen")
    choice: int = int_valid(input("Enter the task's number you want to perform: "))

    if choice == 1:
        logger.info("User wants to see information")
        logger.info("Taking inppput for arguments.")

        user: str = input("Enter the username: ")
        recent_count: int = int_valid(
            input("Enter the number of most recent repos to consider: "),
            num_range=range(1, 101),
        )

        logger.info("Inputed the arguments and have validated it.")
        logger.debug("The arguments are: user=%s, recent_count=%s", user, recent_count)

        return {"todo": TaskType.INFORMATION, "user": user, "count": recent_count}

    elif choice == 2:
        logger.info("User wants to provide the Github token")
        logger.info("Taking env file's path input and validating it.")
        path: Path = path_valid(input("Enter the path to the env file: "))

        logger.info("The path has been inputted and is valid")
        logger.debug("The path: %s", path)
        return {"todo": TaskType.TOKEN, "path": path}

    else:
        logger.info("User wants to do nothing, ie, exit")
        return {"todo": TaskType.EXIT}


def cli_input() -> dict[str, TaskType | str | int | Path | None]:
    args: argparse.Namespace = _parsering_cli_input()

    user = args.user
    recent_count = args.recent_count
    token_path = args.token_path
    load: dict[str, Any] = {"todo": TaskType.EXIT}

    if user is None and token_path is None:
        logger.info("No agruments were provided")
        load = _prompt_input()

    elif token_path is not None:
        logger.info("Validating the path provided for token.")
        env_path: Path = path_valid(args.token_path)

        logger.info("Path for github token was provided")
        logger.debug("Provided source path: %s", args.token_path)
        load = {"todo": TaskType.TOKEN, "path": env_path}

    elif user is not None:
        username: str = str(user)

        if recent_count is None:
            recent_count: int = 5
        else:
            recent_count: int = int_valid(recent_count)

        load = {"todo": TaskType.INFORMATION, "user": username, "count": recent_count}

    return load


# Output functions
def _display_public_repo_table(repos: list[dict[str, str | bool | int]]) -> None:
    table = Table(title="Public Repositres", header_style="bold cyan")

    table.add_column("S.No.", style="dim", justify="right")
    table.add_column("Name", style="bold white", justify="left")
    table.add_column("Stars", style="yellow", justify="right")
    table.add_column("Last Pushed", justify="center", style="green")
    table.add_column("Forked?", style="white", justify="center")

    for i, vals in enumerate(repos, 1):
        table.add_row(
            f"{i}",
            f"{vals["name"]}",
            f"{vals["stars"]}",
            f"{vals["pushed"]}",
            f"{vals["forked"]}",
        )

    console.print(table)


def _display_stats_table(stats: list[dict[str, str | bool | int]]) -> None:
    table = Table(title="Oeral Stats of Repositres", header_style="bold cyan")

    table.add_column("S.No.", style="dim", justify="right")
    table.add_column("Name", style="bold white", justify="left")
    table.add_column("Stars", style="yellow", justify="right")
    table.add_column("Language", style="green", justify="center")
    table.add_column("Untouched", style="white", justify="center")

    for i, vals in enumerate(stats, 1):
        table.add_row(
            f"{i}",
            f"{vals["name"]}",
            f"{vals["stars"]}",
            f"{vals["language"]}",
            f"{vals["untouched"]}",
        )

    console.print(table)


def _display_lang_stat_table(lang_stats: dict[str, float]) -> None:
    table = Table(title="Language Stats of Repositres", header_style="bold cyan")

    table.add_column("S.No.", style="dim", justify="right")
    table.add_column("Language", style="bold white", justify="left")
    table.add_column("% of Total Bytes", style="yellow", justify="right")

    for i, (lang, percent) in enumerate(lang_stats.items(), 1):
        table.add_row(
            f"{i}",
            f"{lang}",
            f"{percent:.2f}",
        )

    console.print(table)


def _display_rate_limit(rate_limits: dict[str, str]) -> None:
    if len(rate_limits) <= 3:
        print("Using cached data, so no rate limit checked")
        return

    content = (
        f"[bold]Total Rate Limit:[/bold]        [cyan]{rate_limits.get('total', 'N/A')}[/cyan]\n"
        f"[bold]Rate Limit Used:[/bold]         [yellow]{rate_limits.get('totlal left', 'N/A')}[/yellow]\n"
        f"[bold]Time Left Till Reset:[/bold]     [green]{rate_limits.get('time left', 'N/A')}[/green]"
    )

    panel = Panel(
        content,
        title="[bold]GitHub Rate Limit Status[/bold]",
        border_style="cyan",
        padding=(1, 2),  # (top/bottom, left/right)
    )
    console.print(panel)


def cli_output(information: dict[str, dict[str, Any]]) -> None:
    repos = information["repos"]["response"]
    stats = information["stats"]["stats"]
    lang_stats = information["lang_stats"]["languages"]
    rate_limits = information["rate_limits"]

    functions = {
        _display_public_repo_table: repos,
        _display_stats_table: stats,
        _display_lang_stat_table: lang_stats,
        _display_rate_limit: rate_limits,
    }

    for func, args in functions.items():
        func(args)

    print("Thankls for using this program.")

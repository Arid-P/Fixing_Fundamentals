import logging
from sys import exit
from os import getenv
from typing import Any
from dotenv import load_dotenv
from shutil import copy
from pathlib import Path

from icecream import ic  # To debug

from utilis import TaskType, setup_logging, get_logger
from cli import cli_input

logger: logging.Logger = get_logger(__name__)
# ic.disable()


def establish_env_token(source_file: Path, env_path: Path, tries: int = 1) -> None:
    if not source_file.exists():
        logger.info("Source file does not exits")
        exit(f"No file exits at {source_file}")

    logger.info("Lodding the source env file and the token")
    load_dotenv(source_file)

    source_token: str | None = getenv("GITHUB_TOKEN")
    logger.info("Loaded the source env file and its token")

    if source_token is None:
        logger.info("The token in the soruce file is None")
        exit("The provided env file has no token")

    logger.info("Creating the program's env file and copying the source file's content")
    logger.debug("The program's env file path: %s", env_path)
    env_path.mkdir(parents=True, exist_ok=True)

    copy(source_file, env_path)
    logger.info("Source file's content were copied to the program's env")

    logger.info("Lodding the program's env file and the token")

    load_dotenv(env_path, override=True)
    program_token: str | None = getenv("GITHUB_TOKEN")

    logger.info("Loaded the program' env file and its token")

    if source_token != program_token:
        logger.info("The source token, and copied token dont match")

        if tries > 1:  # Max tries are 2
            exit(
                "The copying of env file was not successful, the copied token and the provided token were not same"
            )
        else:
            logger.info("Trying again to establish the env")
            establish_env_token(source_file=source_file, env_path=env_path, tries=2)

    del source_file, source_token, program_token, env_path
    return


def load_token(env_path: Path) -> str | None:
    logger.info("Loading the Github token")

    load_dotenv(env_path)
    token: str = getenv("GITHUB_TOKEN")  # type: ignore

    logger.info("The github token was loaded")
    return token


def main() -> None:
    """It is the starting function. From it you can understand a basic flow of the whole program"""
    setup_logging(verbose=True)
    logger.info("Estabished looging")

    env_path = Path(Path(__file__).resolve().parent, "data", ".env")
    load: dict[str, TaskType | str | int | Path] = cli_input()

    if load["todo"] is TaskType.EXIT:
        logger.info("User wants to exit")
        print("Exitting...")
        exit()

    elif load["todo"] == TaskType.TOKEN:
        logger.info("Making the program's env file form the provided path.")

        establish_env_token(load["path"], env_path)  # type: ignore
        print("The token was successfully retrieved")

        logger.info("The program's env file was created adn the token is accessible.")

    elif load["todo"] is TaskType.INFORMATION:
        logger.info("User wants the infromation")

        username = load["user"]
        recent_count = load["count"]
        token = load_token(env_path=env_path)


if __name__ == "__main__":
    main()

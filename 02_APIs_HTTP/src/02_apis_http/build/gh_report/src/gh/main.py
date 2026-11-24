import logging
from sys import exit
from os import getenv
from typing import Any
from dotenv import load_dotenv
from shutil import copy
from pathlib import Path

from paths import env_path
from cli import cli_input, cli_output
from processing import get_payload, user_summary
from utilis import TaskType, setup_logging, get_logger

logger: logging.Logger = get_logger(__name__)
# ic.disable()


def load_token(path: Path, name: str) -> str | None:
    logger.info("Loading the Github token for %s", name)
    logger.debug("Path: %s", path)

    try:
        load_dotenv(path, override=True)
        token: str = getenv("GITHUB_TOKEN")  # type: ignore

        logger.info("The github token was loaded for %s", name)
        return token
    except FileNotFoundError:
        logger.info("The env file does not exits")
        return None


def establish_env_token(source_file: Path, env_path: Path, tries: int = 1) -> None:
    logger.info("Establishing the env file")

    source_token: str | None = load_token(source_file, "provided path")
    if source_token is None:
        logger.info("The token in the soruce file is None")
        exit("The provided env file has no token")

    logger.info("Creating the program's env file and copying the source file's content")
    logger.debug("The program's env file path: %s", env_path)

    copy(source_file, env_path)
    logger.info("Source file's content were copied to the program's env")

    program_token: str | None = load_token(env_path, "program's token")

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


def main() -> None:
    """It is the starting function. From it you can understand a basic flow of the whole program"""
    setup_logging(verbose=True)
    logger.info("Estabished looging")

    token = load_token(env_path, "processing.py testing")

    load: dict[str, TaskType | str | int | Path | None] = cli_input()

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
        logger.info("User wants infromation")

        username: str = load["user"]  # type: ignore
        recent_count: int = load["count"]  # type: ignore
        token: str | None = load_token(path=env_path, name="processing")

        information: dict[str, dict[str, Any]] = get_payload(
            username=username, recent_count=recent_count, token=token
        )
        user_summary(username=username, information=information)
        cli_output(information=information)


if __name__ == "__main__":
    main()

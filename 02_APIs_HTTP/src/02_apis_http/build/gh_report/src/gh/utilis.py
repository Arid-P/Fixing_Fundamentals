import logging
from typing import Literal
from pathlib import Path
from sys import exit
from enum import Enum, auto

from icecream import ic


class TaskType(Enum):
    INFORMATION = auto()
    TOKEN = auto()
    EXIT = auto()


def setup_logging(verbose: bool = False) -> None:
    level: Literal[10] | Literal[20] = logging.DEBUG if verbose else logging.INFO
    file: Path = Path(__file__).parent.parent.parent / "data" / "logs"
    ic(file)
    file.mkdir(parents=True, exist_ok=True)
    file = file / "app.log"
    ic(file)
    file.touch()

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(funcName)s | %(message)s",
        filename=file,  # The file where logs will be saved
        filemode="a",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def get_logger(name: str) -> logging.Logger:
    logger: logging.Logger = logging.getLogger(name=name)
    return logger


logger = get_logger(__file__)


def int_valid(val, tries: int = 2, num_range: range | None = None) -> int:
    err_msg: str = "Some Error has occured"

    for i in range(tries):
        logger.info("Try %s", i)

        try:
            val = int(val)

            if num_range is not None and val not in num_range:
                raise ValueError

            logger.info("The value is a intger and in range")
            logger.debug("The value provided is %s", val)

            return val

        except TypeError:
            logger.info("The value provided is not a integer")
            err_msg = "Error: the value provided is not integer as it was suppose to be"

            val = input(
                "Unforunately the value you enter is not intger.\nSo, please again enter the value: "
            )

        except ValueError:
            logger.info("The value provied is not in range")
            err_msg = "Error: the value provided is not in range"

            val = input(
                "Unforunately the value you enter is not in range. So, please again enter the value: "
            )
    else:
        logger.info("exiting with message: '%s'", err_msg)
        logger.debug("Arguments provided: val=%s, range=%s", val, num_range)
        exit(err_msg)


def path_valid(path: str, tries: int = 2) -> Path:
    err_msg: str = "Some error occured"

    for i in range(tries):
        logger.info("Try %s", i)

        try:
            path_converted: Path = Path(path)
            return path_converted
        except Exception:
            logger.info("The provided path's str is not correct")
            err_msg = "Error: the format in which the path is provided is invalid."

            print("The provided path is not valid. Provided the path again.")
            path = input("Path: ")
    else:
        logger.info("Exitted message: '%s'", err_msg)
        logger.debug("Arguments: pat=%s", path)

        exit(err_msg)

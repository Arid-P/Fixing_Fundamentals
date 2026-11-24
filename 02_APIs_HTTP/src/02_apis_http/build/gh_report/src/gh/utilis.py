import logging
import requests
from typing import Literal
from pathlib import Path
from sys import exit
from enum import Enum, auto
from typing import Any

from icecream import ic

from paths import log_file


class TaskType(Enum):
    INFORMATION = auto()
    TOKEN = auto()
    EXIT = auto()


def setup_logging(verbose: bool = False) -> None:
    level: Literal[10] | Literal[20] = logging.DEBUG if verbose else logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(funcName)s | %(message)s",
        filename=log_file,  # The file where logs will be saved
        filemode="a",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def get_logger(name: str) -> logging.Logger:
    logger: logging.Logger = logging.getLogger(name=name)
    return logger


logger = get_logger(__file__)


def api_failure_handler(
    api_payload: dict[str, Any], payload: dict[str, Any]
) -> tuple[dict[str, Any], bool]:
    # faliure cases
    if api_payload["status code"] == 304:
        logger.info(
            "Status Code 304 was returned. So no change in data, hence cache used"
        )
        payload["cache"] = True
    elif isinstance(api_payload["error"], requests.Timeout) or isinstance(
        api_payload["error"], requests.ConnectionError
    ):
        logger.info("Network error has occured. API could not be reached")
        logger.debug("The error: %s", api_payload["error"])
        print(
            "Network error: Could not reach GitHub API. Falling back to offline cache if available."
        )
        payload["cache"] = True

    elif isinstance(api_payload["error"], requests.HTTPError):
        if api_payload["status code"] == 401:
            logger.info(
                "HTTPERROR has occured. Invalid Github Token. status code: %s",
                api_payload["status code"],
            )
            print("Invalid GITHUB_TOKEN provided in .env.")
        elif api_payload["status code"] == 404:
            logger.info(
                "HTTPERROR has occured. Username provided does not exist. status code: %s",
                api_payload["status code"],
            )
            print(
                f"Error: User '{api_payload["request"].url}' does not exist on GitHub."
            )
        else:
            logger.info(
                "HTTPERROR has occured. Rate Limit exceeded. status code: %s",
                api_payload["status code"],
            )
            print("Rate limit exceeded.")

        logger.debug("The error: %s", api_payload["error"])
        payload["cache"] = True

    elif isinstance(api_payload["error"], requests.JSONDecodeError):
        logger.info("The Json received is not processable")
        print("Error: Received malformed response from server")
        payload["cache"] = True

    return payload, payload["cache"]


def int_valid(val, tries: int = 2, num_range: range | None = None) -> int:
    err_msg: str = "Some Error has occured"

    for i in range(tries):
        logger.info("Try %s", i)

        try:
            val = int(val)

            if num_range is not None and val not in num_range:
                raise AttributeError

            logger.info("The value is a intger and in range")
            logger.debug("The value provided is %s", val)

            return val

        except TypeError:
            logger.info("The value provided is not a integer")
            err_msg = "Error: the value provided is not integer as it was suppose to be"

            val = input(
                "Unforunately the value you enter is not intger.\nSo, please again enter the value: "
            )

        except AttributeError:
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

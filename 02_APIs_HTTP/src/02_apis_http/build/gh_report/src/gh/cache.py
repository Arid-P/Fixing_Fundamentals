from datetime import datetime as dt
import logging
from sys import exit
from typing import Any
from pathlib import Path
from json import load, dump
from os import replace
from shutil import copy

from icecream import ic

from utilis import get_logger
from paths import cache_files

logger: logging.Logger = get_logger(__name__)


def get_cached_repos_stats():
    cache: dict[str, dict[str, Any]] = {}

    for file in cache_files[1:]:
        with open(file, "r") as fh:
            if file.stat().st_size > 0:
                content: dict[str, Any] = load(fh)
            else:
                content = {}

        cache[file.name.split(".")[0]] = content

    return cache


def get_cached_repos() -> dict[str, Any]:
    file = cache_files[0]

    with open(file, "r") as fh:
        if file.stat().st_size > 0:
            all_repos: dict[str, Any] = load(fh)
        else:
            all_repos = {}

    return all_repos


def _write_update_cache_data(file: Path, cache_data: dict[str, Any]) -> bool:
    try:
        logger.info("Updating the cache for %s", file.name)

        BACKUP_FILE = file.parent / f"{file.name}.backup"
        TEMP_FILE = file.parent / f"{file.name}.tmp"

        if not BACKUP_FILE.exists():
            BACKUP_FILE.touch()
        if not TEMP_FILE.exists():
            TEMP_FILE.touch()

        logger.info("Backup and Temperary files have been created")
        logger.debug("Paths: %s, %s", BACKUP_FILE, TEMP_FILE)

        copy(file, BACKUP_FILE)
        logger.info("Backed up the old cache")

        with open(
            TEMP_FILE, "w"
        ) as fh:  # Since file always exists as created in paths.py
            dump(cache_data, fh, indent=4, default=str)
        logger.info("Wrote to temperory cache file")

        replace(TEMP_FILE, file)
        logger.info("Replaced old cache file with the temperary file.")

        return True
    except Exception as e:
        logger.info("Some internal error occured while copying")
        logger.error("Error: %s", exc_info=True)
        return False


def update_cache(agg_data: dict[str, dict[str, Any]]):
    unwritten_files = []

    for file in cache_files:
        name = file.name.split(".")[0]
        cache_data: dict[str, Any] = agg_data[name] if isinstance(agg_data[name], dict) else {"stats": agg_data[name]}
        cache_data["time"] = dt.now()

        written: bool = _write_update_cache_data(file=file, cache_data=cache_data)
        if not written:
            unwritten_files.append(file)

    if len(unwritten_files) != 0:
        return False

    return True

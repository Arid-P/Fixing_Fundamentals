from icecream import ic
from sys import path
from pathlib import Path

build_path = Path(__file__).resolve().parent.parent
path.append(str(build_path))

from build.fetcher_core import fetch_json  # type: ignore


def main() -> None:
    """It is the starting function. From it you can understand a basic flow of the whole program"""

    page_count = 3
    pages = {}

    url = r"https://pokeapi.co/api/v2/pokemon?limit=10&offset=0"
    for num in range(page_count):
        resp: dict | list | None = fetch_json(url=url)
        pages.update({f"Page {num}": resp.get("results")})  # type: ignore

        url = resp.get("next")  # type: ignore

    for page, content in pages.items():
        print(f"{page}\n{content}\n\n")


if __name__ == "__main__":
    main()

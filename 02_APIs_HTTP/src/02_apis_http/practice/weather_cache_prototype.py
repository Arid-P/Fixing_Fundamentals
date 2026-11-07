from icecream import ic

from pathlib import Path
from json import load, dump
from datetime import datetime as dt

from fetcher_core import fetch_json  # type: ignore

PARENT_DIR: Path = Path(__file__).parent
# So that data folder is inside build
CACHE_DIR_R: Path = Path("data", "cache")
CACHE_DIR: Path = PARENT_DIR / CACHE_DIR_R

CACHE_DIR.mkdir(parents=True, exist_ok=True)


def write_resp(file: Path, resp: dict | None) -> bool:
    ic("Writing")
    if isinstance(resp, type(None)): raise LookupError("No response from the server") #to handle the case when resp if None

    content = {
        "time": dt.now(),
        "response": resp
    }
    
    try:
        with open(file, "w") as fh:
            dump(content, fh, default=str)

    except FileNotFoundError:
        open(file, "x").close()
        return False

    return True


def check_load_data(file: Path) -> dict | None:
    content: dict[str, str | dict] = {}

    if (not file.exists()) or file.stat().st_size == 0:
        return None
    
    with open(file,'r') as fh:
        if file.stat().st_size > 0:
            content = load(fh)

    time_diff = dt.now() - dt.strptime(content.get('time'), '%F %T.%f') # type: ignore

    if time_diff.days > 1:
        return None
    
    return content.get('response', None) # type: ignore


def main() -> None:
    """It is the starting function. From it you can understand a basic flow of the whole program"""

    cord: dict[str, tuple[float, float, str]] = {
        "New Delhi": (28.6139, 77.2090, "delhi"),
        "Sitapur (UP)": (27.5751, 80.6638, "sitapur"),
        "Bangalore": (12.9716, 77.5946, "bangalore"),
    }

    url = r"https://api.open-meteo.com/v1/forecast"

    for name, info in cord.items():
        lat, lng, file = info
        cache_file: Path = CACHE_DIR / f"{file}.json"

        data = check_load_data(cache_file)

        if isinstance(data, type(None)):
            params = {
                "latitude": lat,
                "longitude": lng,
                "current": "temperature_2m,weather_code",
                "daily": "temperature_2m_max,temperature_2m_min",
                "timezone": "auto",
            }

            resp: dict | None = fetch_json(url=url, params=params) 
            
            while not write_resp(cache_file, resp):
                ...
        else:
            resp = data

        print(f"{name}\nThe current temperature is {resp.get('current').get('temperature_2m')} C, \nThe maximum temperature today will be {max(resp.get('daily').get('temperature_2m_max'))} C, \nThe minimum temperature today will be {min(resp.get('daily').get('temperature_2m_min'))} C.")  # type: ignore
        print()


if __name__ == "__main__":
    main()


"""

1. New Delhi

• Latitude: 28.6139° N (or 28.644800)
• Longitude: 77.2090° E (or 77.216721)
• Source/Details: New Delhi Coordinates on LatLong.net

2. Sitapur, Uttar Pradesh

• Latitude: 27.5751° N (27.575090)
• Longitude: 80.6638° E (80.663765)
• Source/Details: Sitapur Coordinates on LatLong.net

3. Bengaluru (Bangalore), Karnataka

• Latitude: 12.9716° N (12.971599)
• Longitude: 77.5946° E (77.594566)
• Source/Details: Bengaluru Coordinates on LatLong.net

"""

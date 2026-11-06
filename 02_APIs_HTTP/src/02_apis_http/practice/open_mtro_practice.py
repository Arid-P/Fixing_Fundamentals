from icecream import ic
from sys import path
from pathlib import Path

build_path = Path(__file__).resolve().parent.parent
path.append(str(build_path))

from build.fetcher_core import fetch_json  # type: ignore


def main() -> None:
    """It is the starting function. From it you can understand a basic flow of the whole program"""

    cord: dict[str, tuple[float, float]] = {
        "New Delhi": (28.6139, 77.2090),
        "Sitapur (UP)": (27.5751, 80.6638),
        "Bangalore": (12.9716, 77.5946),
    }

    url = r"https://api.open-meteo.com/v1/forecast"

    for name, crd in cord.items():
        lat, lng = crd
        params = {
            "latitude": lat,
            "longitude": lng,
            "current": "temperature_2m,weather_code",
            "daily": "temperature_2m_max,temperature_2m_min",
            "timezone": "auto",
        }

        resp: dict | list | None = fetch_json(url=url, params=params)

        print(f"{name}\nThe current temperature is {resp.get('current').get('temperature_2m')} C, \nThe maximum temperature today will be {max(resp.get('daily').get('temperature_2m_max'))} C, \nThe minimum temperature today will be {min(resp.get('daily').get('temperature_2m_min'))} C.") # type: ignore
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

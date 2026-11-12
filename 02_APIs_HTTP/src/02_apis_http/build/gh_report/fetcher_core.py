import time
import requests


def wait(retry: int) -> None:
    wait_time = 2**retry
    print(f"Retrying after a wait of {wait_time} seconds.", end=" ", flush=True)

    time.sleep(wait_time)
    print("Retrying", flush=True)


def fetch_json(
    url: str, params: dict | None = None, max_retries: int = 3, timeout: float = 5.0
) -> dict | list | None:
    with requests.Session() as session:
        resp, err = None, None  # to keep resp in in bounds
        
        for retry in range(max_retries):
            try:
                resp = session.get(url, timeout=timeout, params=params)
                resp.raise_for_status()
                return resp.json()

            except (requests.ConnectionError, requests.Timeout):
                if retry == max_retries - 1:
                    raise
                wait(retry)

            except requests.HTTPError:
                if resp.status_code in [429, 503]:  # type: ignore
                    if retry == max_retries - 1:
                        raise
                    wait(retry)
                else:
                    raise


def main() -> None:
    """It is the starting function. From it you can understand a basic flow of the whole program"""
    # sucessful try
    js = fetch_json("https://httpbin.org/json", max_retries=2, timeout=3)
    print(js)

    js1 = fetch_json("https://httpbin.org/delay/4", max_retries=5, timeout=3)
    js2 = fetch_json("https://httpbin.org/status/404", max_retries=5, timeout=3)
    print(js1, js2, sep="\n\n")


if __name__ == "__main__":
    main()

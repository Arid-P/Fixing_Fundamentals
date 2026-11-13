import time
import requests


def wait(retry: int) -> None:
    wait_time = 2**retry
    print(f"Retrying after a wait of {wait_time} seconds.", end=" ", flush=True)

    time.sleep(wait_time)
    print("Retrying")


def fetch(
    url: str,
    params: dict | None = None,
    headers: dict | None = None,
) -> dict:
    max_retries: int = 3
    timeout: float = 5.0

    # to keep them in bound in
    resp: requests.Response = requests.Response()
    data = requests.Response().json()
    err: (
        requests.ConnectionError
        | requests.Timeout
        | requests.HTTPError
        | requests.JSONDecodeError
        | None
    ) = None

    with requests.Session() as session:
        for retry in range(max_retries):
            try:
                resp = session.get(url, headers=headers, params=params, timeout=timeout)

                resp.raise_for_status()
                data = resp.json()

            except (requests.ConnectionError, requests.Timeout) as e:
                err = e
                if retry != max_retries - 1:
                    wait(retry)

            except requests.HTTPError as e:
                err = e
                if resp.status_code in [401, 403, 404, 429]:
                    break

            except requests.JSONDecodeError as e:
                err = e
                data = None

    return {
        "status code": resp.status_code,
        "error": err,
        "header": resp.headers,
        "data": data,
    }


def main() -> None:
    """It is the starting function. From it you can understand a basic flow of the whole program"""
    ...


if __name__ == "__main__":
    main()

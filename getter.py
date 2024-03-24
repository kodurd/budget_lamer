import pandas as pd
import requests
from requests import HTTPError, RequestException


def connect_api(url: str, method: str, headers: dict = None,
                params: dict = None, json: dict = None, data: dict = None) -> requests.Response:
    """Sends get and post requests to the API
    :param url: link to connect to the API
    :param method: can be GET or POST depending on the required method
    :param headers: request headers
    :param params: request parameters (usually passed to get)
    :param json: json request (usually passed in a post)
    :param data:
    :return requests.Response:
    """

    methods = {
        "GET": requests.get,
        "POST": requests.post
    }

    request_method = methods.get(method.upper())
    if not request_method:
        raise ValueError("Method can only accept GET or POST")

    try:
        response = request_method(url=url, headers=headers, params=params, json=json, data=data)
        response.raise_for_status()
        return response
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except RequestException as req_err:
        print(f"Network error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


def get_data_moex(url: str, tickers: list) -> pd.DataFrame:
    """Get data from the MOEX API for the transmitted ticker list"""
    dataframes = []
    for ticker in tickers:
        response = connect_api(url=url.replace('ticker', ticker),
                               method='GET').json()
        data = pd.DataFrame([{k: r[i]
                            for i, k in enumerate(response['aggregates']['columns'])}
                            for r in response['aggregates']['data']])
        dataframes.append(data)

    return pd.concat(dataframes, ignore_index=True)

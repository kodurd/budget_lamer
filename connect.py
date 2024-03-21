import requests
from requests import HTTPError, RequestException


def connect_api(url: str, method: str, headers: dict = None,
                params: dict = None, json: dict = None) -> requests.Response:
    """
    Sends get and post requests to the API
    :param url: link to connect to the API
    :param method: can be GET or POST depending on the required method
    :param headers: request headers
    :param params: request parameters (usually passed to get)
    :param json: json request (usually passed in a post)
    :return requests.Response:
    """

    methods = {
        "GET": requests.get,
        "POST": requests.post
    }

    request_method = methods.get(method.upper())
    if not request_method:
        raise ValueError("Method can only accept GET or POST")

    # Send query
    try:
        response = request_method(url=url, headers=headers, params=params, json=json)
        response.raise_for_status()
        return response
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except RequestException as req_err:
        print(f"Network error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

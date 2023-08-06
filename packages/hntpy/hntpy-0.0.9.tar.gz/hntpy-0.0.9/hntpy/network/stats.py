from hntpy.helium_client import HeliumClient
from typing import Union

# for these requests, we don't want to have to instantiate a class to be able to call methods,
# so keep these functions at the file level

client = HeliumClient()
BASE_URL = "stats"


def get_blockchain_stats() -> dict:
    """Retrieve stats for the blockchain"""
    url = BASE_URL
    return client.get_data(url)


def get_token_supply(format: str = "json") -> Union[dict, str]:
    """Returns the circulating token supply

    Notes:
        - `format` arg can either be "json" or "raw"
        - if "raw" format requested, returns a string value of the token supply number
    """
    url = BASE_URL + "/token_supply"

    # validate format value by turning it to all lowercase, just in case
    format = format.lower()
    format = format if format in ("json", "raw") else "json"
    params = {"format": format}

    return client.get_data(url, params=params)

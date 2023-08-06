from abc import ABC

import aiohttp
from aiohttp import ClientSession, ClientResponse
from json import loads

HEADERS = {"age": "1",
  "cache-control": "public,max-age=3600",
     "content-encoding": "br",
     "content-type": "application/json; charset=utf-8",
     "date": "Fri, 09 Dec 2022 14:55:28 GMT",
     "expires": "Fri, 09 Dec 2022 15:55:28 GMT",
     "last-modified": "Fri, 09 Dec 2022 14:00:00 GMT",
     "server": "Netlify",
     "vary": "Accept-Encoding",
     "x-frame-options": "DENY",
     "x-nf-request-id": "01GKVP4NPWTQDY9RR546NQ97QW",
    "Accept-Language": "en-US,en;q=0.5"}


def get_parameters(parameters: dict[str, str | int] = None) -> dict:
    parameters_without_null = {}

    if parameters is None:
        parameters = {}

    for parameter in parameters:
        value = parameters[parameter]
        if value is not None:
            parameters_without_null[parameter] = value
    return parameters_without_null


class Requestable(ABC):
    def __init__(self, url: str, headers=None):
        self.url = url
        self.headers = headers or HEADERS

    async def get_json(self, request: str, method: str = "GET", parameters: dict[str, str | int] = None, **kwargs) -> dict[str, ...]:
        url = f"{self.url}/{request}"

        async with ClientSession(headers=self.headers) as session:
            async with session.request(url=url, method=method, params=get_parameters(parameters), **kwargs) as response:
                return await response.json()

    async def get_text(self, request: str, method: str = "GET", parameters: dict[str, str | int] = None, **kwargs) -> str:
        url = f"{self.url}/{request}"

        async with ClientSession(headers=self.headers) as session:
            async with session.request(url=url, method=method, params=get_parameters(parameters), **kwargs) as response:
                return await response.text()


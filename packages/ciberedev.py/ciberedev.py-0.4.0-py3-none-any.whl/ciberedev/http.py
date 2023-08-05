import asyncio
import logging
import re
from io import BytesIO
from typing import Literal, Optional, Union
from urllib.parse import urlencode

from aiohttp import ClientResponse, ClientSession

from .errors import InvalidURL, UnableToConnect, UnknownError
from .screenshot import Screenshot
from .searching import SearchResult

HTTP_LOGGER = logging.getLogger("ciberedev.http")
LOGGER = logging.getLogger("ciberedev")

__all__ = []


URL_REGEX = re.compile(
    r"^(?:http|ftp)s?://"
    r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    r"(?::\d+)?"
    r"(?:/?|[/?]\S+)$",
    re.IGNORECASE,
)


class Parameters:
    def __init__(self):
        self._internal = {}

    def __getitem__(self, key: str) -> Optional[str]:
        return self._internal.get(key)

    def __setitem__(self, key: str, value: str) -> None:
        self._internal[key] = value

    def unpack(self) -> dict:
        return self._internal


class QueryParams(Parameters):
    pass


class Headers(Parameters):
    pass


class Route:
    def __init__(
        self,
        *,
        method: Literal["POST", "GET"],
        endpoint: str,
        headers: Optional[Headers] = None,
        query_params: Optional[QueryParams] = None,
    ):
        self.method = method
        self.endpoint = endpoint
        self.headers = headers or Headers()
        self.query_params = query_params or QueryParams()


class HTTPClient:
    def __init__(self, *, session: Optional[ClientSession]):
        self._session = session

    async def request(self, route: Route) -> ClientResponse:
        if self._session is None:
            self._session = ClientSession()

        headers = route.headers.unpack()
        query_params = route.query_params.unpack()
        url = route.endpoint

        if query_params:
            url += f"?{urlencode(query_params)}"

        HTTP_LOGGER.debug("Request URL: %s", url)
        HTTP_LOGGER.debug("Request Headers: %s", headers)
        HTTP_LOGGER.debug("Request Query Params: %s", query_params)

        res = await self._session.request(route.method, url, headers=headers, ssl=False)

        HTTP_LOGGER.debug("Recieved Status Code: %s", res.status)
        HTTP_LOGGER.debug("Recieved Headers: %s", dict(res.headers))

        if res.status != 429:
            return res
        else:
            endpoint = f"/{route.method.split('/')[-1]}"
            LOGGER.warning(
                f"We are being ratelimited at '{endpoint}'. Trying again in 5 seconds"
            )
            await asyncio.sleep(5)
            return await self.request(route)

    async def take_screenshot(self, url: str, delay: int) -> Screenshot:
        if not re.match(URL_REGEX, "http://www.example.com") is not None:
            raise InvalidURL(url)

        query_params = QueryParams()
        query_params["url"] = url
        query_params["delay"] = str(delay)
        route = Route(
            method="POST",
            endpoint="https://api.cibere.dev/screenshot",
            query_params=query_params,
        )

        response = await self.request(route)
        data = await response.json()
        HTTP_LOGGER.debug("Recieved Data: %s", data)

        if data["status_code"] == 200:
            image_route = Route(method="GET", endpoint=data["link"])
            res = await self.request(image_route)
            _bytes = BytesIO(await res.read())
            screenshot = Screenshot(_bytes=_bytes, url=data["link"])
            return screenshot
        else:
            if data["error"] == "I was unable to connect to the website.":
                raise UnableToConnect(url)
            elif data["error"] == "Invalid URL Given":
                raise InvalidURL(url)
            else:
                raise UnknownError(data["error"])

    async def get_search_results(self, query: str, amount: int) -> list[SearchResult]:
        query_params = QueryParams()
        query_params["query"] = query
        query_params["amount"] = str(amount)
        route = Route(
            method="GET",
            endpoint="https://api.cibere.dev/search",
            query_params=query_params,
        )

        response = await self.request(route)
        data = await response.json()
        HTTP_LOGGER.debug("Recieved Data: %s", data)

        results = []
        for result in data["results"]:
            search_result = SearchResult(data=result)
            results.append(search_result)
        return results

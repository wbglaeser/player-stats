from requests import Response, get
from bs4 import BeautifulSoup
from typing import Optional

from player_stats.models.base_entity import BaseEntity
from player_stats.services.proxy_service import ProxyFetcher


class BaseSpider:
    """Base class for spiders. Provides a method to send a request and cook the soup."""
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'}

    def __init__(self, url):
        self.soup = None
        self.url = url

    def _send_request(self) -> Response:
        proxy = ProxyFetcher.get_proxy()
        response = get(self.url, headers=self.headers, proxies=proxy)
        if response.status_code != 200:
            raise ValueError(f"Request failed with status code {response.status_code}")
        else:
            return response

    def _send_request_with_retry(self, retry_count: int = 3) -> Response:
        response = None
        for _ in range(retry_count):
            try:
                return self._send_request()
            except ValueError:
                pass
        if response is None:
            raise ValueError(f"Request failed after {retry_count} retries")

    def cook_the_soup(self) -> BeautifulSoup:
        response = self._send_request()
        return BeautifulSoup(response.content, 'html.parser')

    def build_entity(self) -> BaseEntity:
        raise NotImplementedError

    def scrape(self) -> Optional[BaseEntity]:
        try:
            self.soup = self.cook_the_soup()
        except ValueError:
            print(f"Could not parse entity with url: {self.url}")
            return None
        return self.build_entity()

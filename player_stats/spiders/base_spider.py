from requests import Response, get
from bs4 import BeautifulSoup
from typing import Optional
import tempfile
import json
from dataclasses import asdict
import pandas as pd

from player_stats.services.gcs_service import GcsService
from player_stats.models.base_entity import BaseEntity
from player_stats.services.proxy_service import ProxyFetcher


class BaseSpider:
    """Base class for spiders. Provides a method to send a request and cook the soup."""
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'}

    def __init__(self, url):
        self.soup = None
        self.entity: Optional[BaseEntity] = None
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

    def scrape(self) -> BaseEntity:
        try:
            self.soup = self.cook_the_soup()
        except ValueError:
            print(f"Could not parse entity with url: {self.url}")
            return None
        return self.build_entity()

    def store_as_json(self) -> None:
        """Stores the entity as json in a temporary file and uploads it to GCS. This is defined here as all
        entities have a straightforward json representation."""
        with tempfile.NamedTemporaryFile() as tmp:
            with open(tmp.name, "w") as fp:
                json.dump(asdict(self.entity), sort_keys=True, indent=4, fp=fp)
            GcsService.upload(f"{self.__class__.__name__}.json", tmp.name)

    def store_as_csv(self) -> None:
        with tempfile.NamedTemporaryFile() as tmp:
            self.entity.convert_to_pd().to_csv(tmp.name, index=False)
            GcsService.upload(f"{self.__class__.__name__}/{self.entity.name}.csv", tmp.name)

    def build_entity(self) -> BaseEntity:
        raise NotImplementedError

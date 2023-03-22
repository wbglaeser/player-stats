from requests import Response, get
from bs4 import BeautifulSoup


class BaseSpider:
    """Base class for spiders. Provides a method to send a request and cook the soup."""
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'}

    def __init__(self, url):
        self.url = url

    def _send_request(self) -> Response:
        response = get(self.url, headers=self.headers)
        if response.status_code != 200:
            raise ValueError(f"Request failed with status code {response.status_code}")
        else :
            return response

    def cook_the_soup(self) -> BeautifulSoup:
        response = self._send_request()
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

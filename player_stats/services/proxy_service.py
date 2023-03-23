import requests
from random import randint


class ProxyFetcher:
    url = 'https://api.proxyscrape.com/v2/?request=getproxies&"\
            "protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&simplified=true'

    @classmethod
    def get_proxy(cls):
        response = requests.get(cls.url)
        proxy_list = response.text.split('\r\n')
        # remove any empty elements from the list
        proxy_list = list(filter(None, proxy_list))
        # return a random proxy from the list
        return {'http': 'http://' + proxy_list[randint(0, len(proxy_list) - 1)]}


if __name__ == '__main__':
    print(ProxyFetcher.get_proxy())

import requests
from bs4 import BeautifulSoup

# specify the URL for the FSV Zwickau team page on Transfermarkt
url = 'https://www.transfermarkt.de/fsv-zwickau/startseite/verein/275'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'}

# send a request to the URL and get the response
response = requests.get(url, headers=headers)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# find the table that contains the player statistics
table = soup.find('table', {'class': 'items'})

# loop through all the rows in the table
for row in table.find_all('tr', {'class': ['odd', 'even']}):
    # get the player name and link to their profile
    name_link = row.find('td', {'class': 'hauptlink'})
    name = name_link.find('a')["title"]
    link = 'https://www.transfermarkt.com' + name_link.find("a", {"title": name})["href"]
    
    # get top level player statistics
    number = row.find('td', {'class': 'zentriert'}).text
    country = row.find('img', {'class': 'flaggenrahmen'})['alt']
    market_value = row.find('td', {'class': 'rechts'}).text

    # follow link to players page
    response = requests.get(link, headers=headers)
    player_soup = BeautifulSoup(response.content, 'html.parser')

    birthDate = player_soup.find('span', {'itemprop': 'birthDate'}).text.strip("\n").strip()
    birthPlace = player_soup.find('span', {'itemprop': 'birthPlace'}).text.strip("\n").strip()
    height = player_soup.find('span', {'itemprop': 'height'}).text.strip("\n").strip()

    stats_1_keys = [x.text for x in player_soup.find_all("span", {"class": "info-table__content info-table__content--regular"})]
    stats_1_values = [x.text for x in player_soup.find_all("span", {"class": "info-table__content info-table__content--bold"})]
    print(dict(zip(stats_1_keys, stats_1_values)))

    stats_2_keys = [x.text for x in player_soup.find_all("span", {"class": "info-table__content info-table__content--regular"})]
    stats_2_values = [x.text for x in player_soup.find_all("span", {"class": "info-table__content info-table__content--bold"})]


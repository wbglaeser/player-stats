from player_stats.spiders.player_spider import PlayerSpider
from player_stats.spiders.team_spider import TeamSpider

url = "https://www.transfermarkt.de/jamal-musiala/profil/spieler/580195"
team_url = "https://www.transfermarkt.de/fc-bayern-munchen/startseite/verein/27"

team_spider = TeamSpider(team_url)
team_spider.scrape()
team_spider.store_as_json()
print(team_spider.entity)

# player_spider = PlayerSpider(url)
# player_spider.scrape()
# player_spider.store_as_json()
# print(player_spider.entity)

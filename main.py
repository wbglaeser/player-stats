from player_stats.spiders.player_spider import PlayerSpider
from player_stats.spiders.team_spider import TeamSpider
from player_stats.spiders.league_spider import LeagueSpider

url = "https://www.transfermarkt.de/jamal-musiala/profil/spieler/580195"
team_url = "https://www.transfermarkt.de/fc-bayern-munchen/startseite/verein/27"
league_url = "https://www.transfermarkt.de/bundesliga/startseite/wettbewerb/L1"

# team_spider = TeamSpider(team_url)
# team_spider.scrape()
# team_spider.store_as_csv()
# print(team_spider.entity)

league_spider = LeagueSpider(league_url)
league_spider.scrape()
league_spider.store_as_csv()
print(league_spider.entity)

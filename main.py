from player_stats.spiders.player_spider import PlayerSpider
from player_stats.spiders.team_spider import TeamSpider

url = "https://www.transfermarkt.de/jamal-musiala/profil/spieler/580195"
team_url = "https://www.transfermarkt.de/fc-bayern-munchen/startseite/verein/27"

team = TeamSpider(team_url)
print(team.scrape())

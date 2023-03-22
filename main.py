from player_stats.spiders.player_spider import PlayerSpider

url = "https://www.transfermarkt.de/jamal-musiala/profil/spieler/580195"

player = PlayerSpider(url)
print(player.build_player())
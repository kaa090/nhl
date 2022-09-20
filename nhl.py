#!/usr/bin/python3
import requests
import jmespath as j
import pandas as pd
from time import sleep

season = "20212022"
stats = {}

teams = requests.get(f"https://statsapi.web.nhl.com/api/v1/teams?expand=team.roster").json()

for team in teams['teams']:
	team_name = team['abbreviation']
	print(f"\t\t{team_name}")

	players = team['roster']['roster']

	try:
		for player in players:

			player_id = player['person']['id']
			player_name = player['person']['fullName']
			player_name2 = player['person']['fullName'].split(' ')
			player_name2 = f"{player_name2[1]}, {player_name2[0]}"
			player_link = player['person']['link']
			player_pos = player['position']['abbreviation']

			print(player_name2)

			player_data = requests.get(f"https://statsapi.web.nhl.com{player_link}/stats?stats=statsSingleSeason&season={season}").json()
			player_stats = player_data['stats'][0]['splits'][0]['stat']
			player_sum = 0

			if len(player_stats) > 0:
				if player_pos == 'G':
					player_sum = player_stats['wins'] + player_stats['goalAgainstAverage'] + player_stats['savePercentage']
				else:
					player_sum = player_stats['goals'] + player_stats['assists'] + player_stats['pim'] + player_stats['powerPlayPoints'] + player_stats['gameWinningGoals'] + player_stats['shots'] + player_stats['hits'] + player_stats['blocked']
				stats[player_id] = [player_name, player_name2, player_pos, player_sum, player_stats]
			else:
				stats[player_id] = [player_name, player_name2, player_pos, player_sum, {}]
	except Exception as e:
		print(str(e))
		print(players)

df = pd.DataFrame.from_dict(stats, orient="index", columns=['name', 'name2', 'pos', 'sum', 'stats'])
df1 = df.reset_index()
df2 = pd.json_normalize(df['stats'].dropna())
df3 = pd.merge(df1, df2, left_index=True, right_index=True).set_index('index').drop('stats', 1)
df3.to_csv(f"nhlstats{season}.csv")

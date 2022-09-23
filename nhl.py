#!/usr/bin/python3
import requests
import pandas as pd

season_1 = "20202021"
season = "20212022"
statsP = {}
statsG = {}
keysP = ['goals', 'assists', 'pim', 'powerPlayPoints', 'gameWinningGoals', 'shots', 'hits', 'blocked',]
keysPn = ['g', 'a', '_pim', 'ppp', 'gwg', '_shots', '_hits', 'blocks',]
keysG = ['wins', 'goalAgainstAverage', 'savePercentage']
keysGn = ['w', 'gaa', 'sp']

def parse_season(url):
	teams = requests.get(url).json()

	for team in teams['teams']:
		team_name = team['abbreviation']
		print(f"\t\t{team_name}")

		players = team['roster']['roster']

		try:
			for player in players:
				pid = player['person']['id']

				if pid in statsP or pid in statsG:
					continue

				name = player['person']['fullName']
				name2 = player['person']['fullName'].split(' ')
				name2 = f"{name2[1]}, {name2[0]}"
				link = player['person']['link']
				pos = player['position']['abbreviation']

				my_statP = dict.fromkeys(keysP, 0)
				my_statG = dict.fromkeys(keysG, 0)

				print(name2)

				player_data = requests.get(f"https://statsapi.web.nhl.com{link}/stats?stats=statsSingleSeason&season={season}").json()

				if player_data['stats'][0]['splits']:
					stat = player_data['stats'][0]['splits'][0]['stat']

					if pos == 'G':
						for key in keysG:
							if key in stat:
								my_statG[key] = stat[key]
						my_statG.update(stat)
						statsG[pid] = [name, name2, pos, team_name, my_statG]
					else:
						for key in keysP:
							if key in stat:
								my_statP[key] = stat[key]
						my_statP.update(stat)
						statsP[pid] = [name, name2, pos, team_name, my_statP]
		except Exception as e:
			print(str(e))

def get_df(stats, keys, keysN):
	df = pd.DataFrame.from_dict(stats, orient="index", columns=['name', 'name2', 'pos', 'team', 'stats'])
	df1 = df.reset_index()
	df2 = pd.json_normalize(df['stats'].dropna())
	df3 = pd.merge(df1, df2, left_index=True, right_index=True).set_index('index').drop('stats', 1)

	df3.insert(4, 'sum', 0)
	for clmn in reversed(keysN):
		df3.insert(5, clmn, 0)
	df3[keysN] = df3[keys].apply(lambda x: (x - x.mean()) / x.std() )

	if 'gaa' in keys:
		df3['gaa'] = -df3['gaa']
	for clmn in keysN:
		df3['sum'] += df3[clmn]
	df3 = df3.sort_values('sum', ascending = False)

	return df3

parse_season("https://statsapi.web.nhl.com/api/v1/teams?expand=team.roster")
parse_season(f"https://statsapi.web.nhl.com/api/v1/teams?expand=team.roster&season={season}")
parse_season(f"https://statsapi.web.nhl.com/api/v1/teams?expand=team.roster&season={season_1}")

dfP = get_df(statsP, keysP, keysPn)
dfG = get_df(statsG, keysG, keysGn)

dfPG = pd.concat([dfP, dfG])
dfPG.to_csv(f"nhl_statsPG_{season}.csv")

# key_all = ['index', 'name', 'name2', 'pos', 'team', 'sum', 'g', 'a', '_pim', 'ppp', 'gwg', '_shots', '_hits', 'blocks', 'goals', 'assists', 'pim', 'powerPlayPoints', 'gameWinningGoals', 'shots', 'hits', 'blocked', 'timeOnIce', 'games', 'w', 'gaa', 'sp', 'wins', 'goalAgainstAverage', 'savePercentage']
# keyP = ['goals', 'assists', 'pim', 'powerPlayPoints', 'gameWinningGoals', 'shots', 'hits', 'blocked']
# keyPn = ['g', 'a', '_pim', 'ppp', 'gwg', '_shots', '_hits', 'blocks']
# keyG = ['wins', 'goalAgainstAverage', 'savePercentage']
# keyGn = ['w', 'gaa', 'sp']

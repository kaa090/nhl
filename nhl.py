#!/usr/bin/python3
import requests
import pandas as pd
from time import sleep

season = "20212022"
statsP = {}
statsG = {}
keysP = ['goals', 'assists', 'pim', 'powerPlayPoints', 'gameWinningGoals', 'shots', 'hits', 'blocked',]
keysPn = ['g', 'a', '_pim', 'ppp', 'gwg', '_shots', '_hits', 'blocks',]
keysG = ['wins', 'goalAgainstAverage', 'savePercentage']
keysGn = ['w', 'gaa', 'sp']

teams = requests.get(f"https://statsapi.web.nhl.com/api/v1/teams?expand=team.roster").json()

for team in teams['teams']:
	team_name = team['abbreviation']
	print(f"\t\t{team_name}")

	players = team['roster']['roster']

	try:
		for player in players:
			pid = player['person']['id']
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
	break

dfP = pd.DataFrame.from_dict(statsP, orient="index", columns=['name', 'name2', 'pos', 'team', 'stats'])
dfP1 = dfP.reset_index()
dfP2 = pd.json_normalize(dfP['stats'].dropna())
dfP3 = pd.merge(dfP1, dfP2, left_index=True, right_index=True).set_index('index').drop('stats', 1)

dfP3.insert(4, 'sum', 0)
for clmn in reversed(keysPn):
	dfP3.insert(5, clmn, 0)
dfP3[keysPn] = dfP3[keysP].apply(lambda x: (x - x.mean()) / x.std() )
for clmn in keysPn:
	dfP3['sum'] += dfP3[clmn]

dfP3.to_csv(f"nhl_statsP_{season}.csv")

dfG = pd.DataFrame.from_dict(statsG, orient="index", columns=['name', 'name2', 'pos', 'team', 'stats'])
dfG1 = dfG.reset_index()
dfG2 = pd.json_normalize(dfG['stats'].dropna())
dfG3 = pd.merge(dfG1, dfG2, left_index=True, right_index=True).set_index('index').drop('stats', 1)

dfG3.insert(4, 'sum', 0)
for clmn in reversed(keysGn):
	dfG3.insert(5, clmn, 0)
dfG3[keysGn] = dfG3[keysG].apply(lambda x: (x - x.mean()) / x.std() )
dfg3['gaa'] = -dfg3['gaa']
for clmn in keysGn:
	dfG3['sum'] += dfG3[clmn]

dfG3.to_csv(f"nhl_statsG_{season}.csv")

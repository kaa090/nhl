#!/usr/bin/python3
import requests
import jmespath as j
import pandas as pd

team_id = 15
season = "20212022"

team_data = requests.get(f"https://statsapi.web.nhl.com/api/v1/teams/{team_id}?expand=team.roster&season={season}").json()

player_info = j.search('teams[*].roster.roster[*].*', team_data)[0]

stats = {}

for player in player_info:
    player_id = j.search('id', player[0])
    player_name = j.search('fullName', player[0])
    player_link = j.search('link', player[0])
    player_data = requests.get(f"https://statsapi.web.nhl.com{player_link}/stats?stats=statsSingleSeason&season={season}").json()
    player_stats = j.search('stats[*].splits[0].stat', player_data)
    if len(player_stats) > 0:
        stats[player_id] = [player_name, player_stats[0]]
    else:
        stats[player_id] = [player_name, {}]


df = pd.DataFrame.from_dict(stats, orient="index", columns=['name', 'stats'])
df1 = df.reset_index()
df2 = pd.json_normalize(df['stats'].dropna())
df3 = pd.merge(df1, df2, left_index=True, right_index=True).set_index('index').drop('stats', 1)
print(df3)
df3.to_csv(f"nhlstats{season}.csv")

#!/usr/bin/python3
import requests
import json

# team triCode:
# https://api.nhle.com/stats/rest/en/team

# roster:
# https://api-web.nhle.com/v1/roster/{triCode}/current

# player stat:
# https://api-web.nhle.com/v1/player/{player_id}/landing

ovi_id = 8471214

def get_player_stat_json(player_id):
	url = f"https://api-web.nhle.com/v1/player/{player_id}/landing"
	return requests.get(url).json()

stat_json = get_player_stat_json(ovi_id)

json_object = json.dumps(stat_json, indent=4)

with open("ovi.json", "w") as outfile:
	outfile.write(json_object)

# with open("ovi.json", "w") as outfile:
#     json.dump(stat_json, outfile)
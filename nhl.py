from nhlstats import list_games, list_plays
from nhlstats.formatters import csv

# List all games today and write all plays from each as a csv file named like the game_id
for game in list_games():  # No args will list all games today
    game_id = game['game_id']
    plays = list_plays(game_id)  # get plays, normalized

    with open('{}.csv'.format(game_id), 'w') as f:
        csv.dump(plays, f)

#!/usr/bin/python3
from nhlstats import list_plays, list_shifts
import pandas as pd

gameid = "2019020418"

plays = pd.DataFrame(list_plays(gameid))
shifts = pd.DataFrame(list_shifts(gameid))

print(plays.head())
shifts.head()

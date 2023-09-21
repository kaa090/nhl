import pandas as pd

indx = ['player']
kfg = ['G', 'A', 'PIM', 'PPP', 'GWG', 'SOG', 'HIT', 'BLK']

df = pd.read_csv("d:/prog/python/yfhl/teams.csv", index_col = indx, usecols = indx+kfg, sep=";")

df['Win'] = 0

for i in range(len(df.index)):
	for j in range(i+1, len(df.index)):
		win_i = 0
		win_j = 0

		for k in kfg:
			if df.at[df.index[i], k] > df.at[df.index[j], k]:
				win_i += 1
			elif df.at[df.index[i], k] < df.at[df.index[j], k]:
				win_j += 1

		if win_i > win_j:
			df.at[df.index[i], 'Win'] += 1			
		elif win_i < win_j:
			df.at[df.index[j], 'Win'] += 1

		print(df.index[i], "-", df.index[j])
		print(win_i, " : ", win_j)

df.sort_values('Win', ascending = False, inplace = True)
print(df)

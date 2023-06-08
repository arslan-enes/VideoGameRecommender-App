import pandas as pd

df = pd.read_csv('MetacriticPCGamesofAllTime.csv')
# df = df.loc[:, ['title', 'critic_reviews']]
df = df.dropna(subset=['critic_reviews','summary'])
df = df.reset_index(drop=True)
df = df.reset_index()
df = df.rename(columns={'index':'_id'})
df.to_csv('MetacriticPCGamesofAllTime.csv', index=False)
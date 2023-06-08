import pandas as pd
import numpy as np

df = pd.read_csv('MetacriticPCGamesofAllTime.csv')

df.critic_reviews = df.critic_reviews.apply(lambda x: eval(x))
df.critic_reviews = df.critic_reviews.apply(lambda x: "".join(x))
df.genres = df.genres.apply(lambda x: eval(x))
df.release_date = pd.to_datetime(df.release_date, format='%b %d, %Y', errors='coerce')
df.loc[df['release_date'].isnull(), 'release_date'] = pd.to_datetime('Jan 1, 1900')

df.replace('tbd', np.nan, inplace=True)
df.user_score = df.user_score.astype(float)

df.user_rating_count.fillna(0, inplace=True)
df.user_rating_count = df.user_rating_count.apply(lambda x: str(x).split()[0])
df.user_rating_count = df.user_rating_count.astype(int)

df.to_dict('records')
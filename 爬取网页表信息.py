import pandas as pd

url = 'http://www.stat-nba.com/player/1717.html'
df = pd.read_html(url)[1]
df.to_csv('JordanD.csv', encoding='utf-8', index=0,header=0)

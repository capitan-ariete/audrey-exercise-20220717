"""The avocado.csv comes from
 https://www.kaggle.com/datasets/neuromusic/avocado-prices?resource=download
"""

from os import getenv

import pandas as pd

import shimoku_api_python as shimoku


api_key: str = getenv('API_TOKEN')
universe_id: str = getenv('UNIVERSE_ID')
business_id: str = getenv('BUSINESS_ID')
environment: str = getenv('ENVIRONMENT')


s = shimoku.Client(
    config={'access_token': api_key},
    universe_id=universe_id,
    environment=environment,
)
s.plt.set_business(business_id=business_id)


df = pd.read_csv('../data/avocado.csv')
# Let's take just some columns to play
df_temp = df[['Date', 'AveragePrice', 'region', 'type']].copy()
# Let's take just total US
df_temp = df_temp[
    (df_temp['region'] == 'TotalUS')
    & (df_temp['type'] == 'organic')
]
# Convert Date column to datetime64
df_temp['Date'] = pd.to_datetime(df_temp['Date'])

menu_path: str = 'Avocado'
s.plt.line(
    data=df_temp, x='Date', y=['AveragePrice'],
    menu_path=menu_path,
    order=0, rows_size=2, cols_size=12,
)


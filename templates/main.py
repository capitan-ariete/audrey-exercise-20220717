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
menu_path: str = 'Avocado'


def create_line_organic_total_us():
    """Some initial play"""
    # Let's take just some columns to play
    df_temp = df[['Date', 'AveragePrice', 'region', 'type']].copy()
    # Let's take just total US
    df_temp = df_temp[
        (df_temp['region'] == 'TotalUS')
        & (df_temp['type'] == 'organic')
    ]
    # Convert Date column to datetime64
    df_temp['Date'] = pd.to_datetime(df_temp['Date'])

    s.plt.line(
        data=df_temp, x='Date', y=['AveragePrice'],
        menu_path=menu_path,
        order=0, rows_size=2, cols_size=12,
    )


def create_price_repetition():
    """
    Trying to create this https://www.kaggleusercontent.com/kf/5545692/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..Vq4iGc7v8E7zNzDQgZMJYQ.BRvHnwXLLxwIDMKYTqcvB1ME6ju1y5uTZ5035MA8OBHC_aWpM5P-BjB5ZZpqrbQafBX6PSr_Qv0xO94ojEY2IsaWETi3610bZX2LZ0Gjr_Rh3udFO08GicWRVFQttPU1QBmlhfqg1yPmY5S2PvltirndFWWmbNperiMo6-bBfzJSDGYMEz_eFR_ii9XtKItQTIv5KBXjiYWjQbTUNorCszVqeRuvlvXnLh6ynTp-qLDSS8GqB0C0604i-ayJkMGIya_nvRP74TsNpTEPPwEBRDveHC_2Y16Ook8mFVb0_UAmUg1V6SBh1z3FlZM2NrA-iBPm2ateNSdFbYcKa-duTcLKhGCS9740hL3gIVc1ii7m6BoKs54QWFTQTu_Lzp-jDz6z8X0uvBKR-CZjAiclepw0bFnC6ATu9724L2NKxpINFezMGkY2svJuWl_WEn4kbW1wGzFlP_YZw2XKS-2wfSoBGsJ9mZepFLVHUX8jhfuAkIZV3RV_p3KvwuF7nGwN3fgH9wHP8YLpB6-9C1Ex1UTXFvELH5qBieWgnLnT6UwSYB2z9BLVrtlhSlMBlerGfE3n_aGNNjx27IuUTA3Pz6q8otdQIxfNZGfjN-XL9XfvMqDtrrUy3_m8h6GssYF8zyK1nK61AQTgarA2hUaXzzBW44lYNVWfvhnz3tm2foOgXsxN3lcRG8QgItZxBXJS.VPexWkv8d9gvJkSf9_OV9w/__results___files/__results___12_0.png
    from this guy https://www.kaggle.com/code/yemregundogmus/avocado-prices-analysis-and-prediction
    :return:
    """
    # Let's take just some columns to play
    df_temp = df[['Date', 'AveragePrice', 'region', 'type']].copy()
    # Let's take just total US
    df_temp = df_temp[
        (df_temp['region'] == 'TotalUS')
        & (df_temp['type'] == 'organic')
    ]
    df_temp['AveragePrice'] = df_temp['AveragePrice'].round(1)
    df_temp = df_temp.groupby('AveragePrice')['Date'].count().reset_index()
    s.plt.bar(
        data=df_temp, x='AveragePrice', y=['Date'],
        menu_path=menu_path,
        order=1, rows_size=2, cols_size=6,
    )


create_line_organic_total_us()
create_price_repetition()

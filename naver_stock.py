import requests
import pandas as pd
import matplotlib.pyplot as plt

# 네이버 주식 일일 종가, 시가 수집
def stock_price(code, page=1, pageSize=60):
    url = f'https://m.stock.naver.com/api/index/{code}/price?pageSize={pageSize}&page={page}'
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)[['closePrice','openPrice']]

# 환율
def exchange_rate(code='FX_USDKRW', page=1, pageSize=60):
    url = f'https://m.stock.naver.com/front-api/marketIndex/prices?category=exchange&reutersCode={code}&pageSize={pageSize}&page={page}'
    response = requests.get(url)
    data = response.json()['result']
    return pd.DataFrame(data)[['localTradedAt','closePrice']]

print(exchange_rate())

# 데이터 전처리
page_size = 30
kp_df = stock_price('KOSPI',pageSize=page_size)
kd_df = stock_price('KOSDAQ',pageSize=page_size)
usd_df = exchange_rate(pageSize=page_size)

kp_df['closePrice'] = kp_df['closePrice'].apply(lambda data: float(data.replace(',', '')))
kd_df['closePrice'] = kd_df['closePrice'].apply(lambda data: float(data.replace(',', '')))
usd_df['closePrice'] = usd_df['closePrice'].apply(lambda data: float(data.replace(',', '')))
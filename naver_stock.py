import requests
import pandas as pd

# 네이버 주식 일일 종가, 시가 수집
def stock_price(code, page=1, pageSize=60):
    url = f'https://m.stock.naver.com/api/index/{code}/price?pageSize={pageSize}&page={page}'
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)[['closePrice','openPrice']]

# 환율
def exchange_rate(code='FX_USDKRW', page=1, page_size=60):
    url = f'https://m.stock.naver.com/front-api/marketIndex/prices?category=exchange&reutersCode={code}&pageSize={page_size}&page={page}'
    response = requests.get(url)
    data = response.json()['result']
    return pd.DataFrame(data)[['localTradedAt','closePrice']]

print(exchange_rate())
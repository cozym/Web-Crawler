import requests
import pandas as pd

def stock_price(code, page=1, pageSize=60):
    url = f'https://m.stock.naver.com/api/index/{code}/price?pageSize={pageSize}&page={page}'
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)[['closePrice','openPrice']]

print(stock_price('KOSPI'))
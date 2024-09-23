import requests
import pandas as pd

pageSize, page = 50, 1
url = f'https://m.stock.naver.com/api/index/KOSPI/price?pageSize={pageSize}&page={page}'

response = requests.get(url)
print(response.text)
import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    kv = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=kv)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    # print(response.text[1000:2000])
except:
    print("error!")

amazon = BeautifulSoup(response.text, 'html.parser')
print(amazon.head.title.attrs)
print(amazon.head.title.navigableString)

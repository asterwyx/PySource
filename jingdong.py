import requests
from bs4 import BeautifulSoup
url = "https://item.jd.com/100000177764.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("发现异常！")
print(type(r))
print(type(r.text))
xsmax = BeautifulSoup(r.text, 'html.parser')
print('divider...')
print(xsmax.prettify())
print(xsmax.title)
tag = xsmax.a
print(tag.parent.name)
print(tag.parent.parent.name)
print(tag.attrs)
print(type(tag))
print(tag.string)

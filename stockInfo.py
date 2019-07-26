# -*- coding:UTF-8 -*-
# -*- Author:Cecil -*-

#'''
#关于本爬虫的可行性分析：
#从东方财富网上获取全网股票编号列表，然后用该编号与我们的百度股市通的url一起构成我们爬取单股信息的url，因为获取html内容的代码相同，可封装为一个getHTMLText相同，
#因为两个网站的html组织方式不同，所以解析要分别进行，就不考虑复用代码。主要所以一共应该有四个函数，最后将获得的信息以字典形式存入我们的本地文件中
#'''
import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    stockList = soup.find_all('a')
    for stock in stockList:
        try:
            href = stock.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}', href)[0])
        except:
            continue

def getStockInfo(lst, fpath, stockURL):
    for stockcode in lst:
        url = stockURL + stockcode + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue # 非空的时候才开始后面的定位解析操作
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find_all('div', attrs={'class':'stock-bets'}) # 定位到存储股票个股信息的标签，股票的全部信息存储在这个标签中的各个子标签
            
            stockName = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':stockName.text.split()[0]}) # 以键值对的形式存入股票的名字
            
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')

            for i in range(len(keyList)):
                key = keyList[i]
                value = valueList[i]
                infoDict[key] = value
            
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n') # 写入文件操作
        except:
            traceback.print_exc()
            continue
    return ""

def main():
    stockListURL = "http://quote.eastmoney.com/stock_list.html"
    stockInfoURL = "https://gupiao.baidu.com/stock/"
    codeList = []
    dictPath = "./stockInfo.txt"
    getStockList(codeList, stockListURL)
    getStockInfo(codeList, dictPath, stockInfoURL)

if __name__ == "__main__":
    main()
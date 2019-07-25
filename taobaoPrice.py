import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url, header={'User-Agent':'Mozilla5.0'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        with open(".\\taobaoxinxi.txt", w) as f:
            f.write(r.text)
        return r.text
    except:
        return ""

def parsePage(ilt, html):
    if html:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        if plt or tlt:
            print("爬取成功！")
        try:
            for i in range(len(plt)):
                price = eval(plt[i].split(':')[1])
                title = eval(tlt[i].split(':')[1])
                if i == 1:
                    print(price,title)
                ilt.append([price, title])
        except:
            print("error")
        if ilt:
            print("存储成功！") # 此处用来检验我们是否成功将信息存储到我们的列表中，如果不是空的列表就会打印出爬取成功语句
    else:
        print("获取的html是空的！")

def printGoodList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = "扩展坞" # 这是我们的搜索关键词，通过传入搜索关键词组成我们的url
# 设定向下一页爬取的深度，这里我们设置为2，也就是说我们只爬取两页的信息
    depth = 2
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = [] # 我们用infoList来存储我们的商品信息
    for i in range(depth):
        try:
            url = start_url + "&s=" +str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodList(infoList)
if __name__ == "__main__":
    main()
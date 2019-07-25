import requests
from bs4 import BeautifulSoup
import bs4 # 主要是导入关于元素类型的定义，在后面的类型判断中起作用
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text # 返回获得的html页面的内容，也就是一个文本类型
    except: 
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td') # tds是一个列表，用来保存我们在每一个tr标签中得到的子标签，每一个tr标签即是一个大学的所有信息
            ulist.append([tds[0].string, tds[1].string, tds[2].string]) # 用一个列表来存储一个大学的所有信息，然后再将这个列表作为ulist的一个元素
def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html" # 将最好大学网的网址用变量url存储起来
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)
if __name__ == "__main__":
    main()
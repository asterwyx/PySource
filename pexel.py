import requests
from lxml import etree

# 1.请求包图网拿到数据
response = requests.get("https://www.pexels.com/")
print(response.text)

# 2.抽取想要数据 视频标题、视频链接
html = etree.HTML(response.text)
tit_list = html.xpath('//span[@class="video-title"]/text()')
src_list = html.xpath('//div[@class="video-play"]/video/@src')
for tit, src in zip(tit_list, src_list):
    # 3.下载视频
    response = requests.get("https:" + src)
    # 4.保存视频
    filename = "video\\" + tit +".mp4"
    print("正在保存视频文件：" + filename)
    with open(filename, "wb") as f:
        f.write(response.content)
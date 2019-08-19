import requests
import re
string = input('请输入想查找的内容')
# 1.确定Url
url = 'https://image.baidu.com/search/flip?tn=baiduimage&word='+string
# 2.请求
text = requests.get(url).text
# 3.筛选数据，分析数据
image_urls = re.findall('"objURL":"(.*?)"', text)
for image_url in image_urls:
    # 设置图片名字，对URL进行切割
    image_name = image_url.split('/')[-1]
    # $表示匹配字符串末尾
    image_result = re.search('(.jpg|.png|.gif|.jpeg|.tif|.ico$)', image_name)
    if not image_result:
        image_name = image_name+'.jpg'
    # print(image_name)
    
    # 下载图片
    image=requests.get(image_url).content
    # 4.保存
    with open('./images/%s'%image_name, 'wb') as file:
        file.write(image)

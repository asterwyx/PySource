import requests
import traceback

if __name__ == '__main__':
    # try:
    #     r = requests.get("https://www.douban.com/")
    #     r.raise_for_status()
    #     r.encoding = r.apparent_encoding
    #     print(r.text)
    # except:
    #     print("Status Error!")

    # url with parameters
    params = {'q': 'python', 'cat': '1001'}
    try:
        r = requests.get("https://www.douban.com/", params=params)
        r.raise_for_status()
        # acquires 'bytes' object
        with open('bi-douban.txt', 'wb') as f:
            f.write(r.content)
        r.encoding = r.apparent_encoding
        print(r.encoding)
        with open('douban.txt', 'w', encoding=r.encoding) as f:
            f.write(r.text)
    except:
        traceback.print_exc()

    # information in json can be directly accessed without parsing
    # try:
    #     r = requests.get("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where"
    #                      "%20woeid%20%3D%202151330&format=json")
    #     print(r.status_code)
    #     r.raise_for_status()
    #     with open('yahooapi_json.txt', 'w') as f:
    #         f.write(r.json())
    # except:
    #     traceback.print_exc()

    #  add headers
    try:
        r = requests.get("https://www.douban.com/",
                         headers={'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.headers)
        print(r.headers['Content-Type'])
        print(r.text)
    except:
        print("Status Error!")
    # 使用data参数在post请求中传入dict形式数据
    # r = requests.post("https://accounts.douban.com/login", data={'form-phonenumber': '18120339968',
    #                                                              'form-password': 'db5201314yx@love'})

    # print(r.text)
    print(r.status_code)

    # 查看cookies
    print(r.cookies)
"""
下面为一些不可执行的示例代码
"""
# requests默认使用application/x-www-form-urlencoded对POST数据编码。
# 可以编辑json参数直接传入json数据
try:
    params = {'key': 'value'}
    r = requests.post("url", json=params)
except:
    pass
# 传入的json参数为dict格式，在内部会自动序列化JSON
# 也可以上传文件，本来是需要更复杂的编码格式，但是在requests模块中只需要将文件当作files参数传递就行
try:
    upload_files = {'file': open('example.xls', 'rb')}
    r = requests.post("url", files=upload_files)
    print(r.cookies['ts'])  # 可以使用这种方式获取特定的cookie
    cs = {'token': '12345', 'status': 'working'}
    r = requests.post("url", cookies=cs)  # 也可以使用这种方式来传入cookies
    r2 = requests.get("url", timeout=2.5)  # 使用以秒为单位的timeout参数来规定超时设置
except:
    pass
# 在读取文件时，务必使用rb模式即二进制模式读取，这样才能保证获取的bytes长度是文件的长度

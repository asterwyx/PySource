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
        with open('douban.txt', 'w') as f:
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

    r = requests.post("https://accounts.douban.com/login", data={'form-phonenumber': '18120339968',
                                                                 'form-password': 'db5201314yx@love'})
    # print(r.text)
    print(r.status_code)

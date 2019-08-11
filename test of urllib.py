from urllib import request

with request.urlopen("https://movie.douban.com/subject/27060077") as f: # urlopen is a function that sends a http or https request and get a response, its parameter can be either a string of url or a Request object
    data = f.read() # returns a bytes object
    print("Status:", f.status, f.reason)
    for k, v in f.getheaders():
        print("%s: %s" % (k, v)) # line by line print headers
    print("Data:", data.decode('utf-8')) # print text of data

# modify headers to simulate iphone 6, we will receive a mobile website
req = request.Request("https://movie.douban.com/subject/27060077")
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:
    data = f.read()
    print("Status:", f.status, f.reason)
    for k, v in f.getheaders():
        print("%s: %s" % (k, v))
    print("Data:", data.decode('utf-8'))

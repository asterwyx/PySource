import chardet

# 使用chardet检测编码
encode = chardet.detect(b'Hello, world')
print(encode)
# 检测用gbk编码的中文
data = "离离原上草，一岁一枯荣".encode('gbk')
encode_information = chardet.detect(data)
print(encode_information)
# 检测用utf-8编码的中文
data1 = "离离原上草，一岁一枯荣".encode('utf-8')
encode_information = chardet.detect(data1)
print(encode_information)
# 尝试检测日文
data2 = "最新の主要ニュース".encode('euc-jp')
encode = chardet.detect(data2)
print(encode)

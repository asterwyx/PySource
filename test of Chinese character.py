import re
regex = re.compile(r"^\d{1:2}[^\x00-\xff][^\x00-\xff][\u4e00-\u9fa5]{2}[^\x00-\xff]$")
rstring = "12日（今天）"
result = regex.match(rstring)
if result:
    print("OK!")
    print(result.group(0))

# 试试用切片处理这个字符串
print(rstring[:4])
query_city = input("Please input your city:")
regex2 = re.compile(r"(\d{9})="+query_city)
result = regex2.match("101010100=北京  ")
if result:
    print("OK!")
    print(result.group(1))
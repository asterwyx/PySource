from io import StringIO
import pickle
d = {'name':'Bob', 'age':20, 'score':88}
print(pickle.dumps(d)) # 将一个变量序列化
f = open('dump.txt', 'wb')
pickle.dump(d, f) # 将一个变量序列化之后直接写到文件对象dump.txt中
f.close()
g = open('dump.txt', 'rb')
e = pickle.load(g) # 运用load()函数直接从一个file-like object中反序列化出对象
g.close()
print(e)

# 用JSON将对象序列化成标准形式（JSON字符串），以便在不同的编程语言之间进行通信
import json # 导入Python内置的json模块，其提供了非常完善的Python对象到JSON格式的转换
f = open('test.txt', 'w')
d2 = dict(name='Bob', age=20, score=88) # 创建一个dict，这个dict包含三个元素
json_str = json.dumps(d2) # 使用dumps函数将整个数据变成json格式字符串并用json_str这个变量接受这个值
json.dump(d2, f)
f.close()
f = open('test.txt', 'r')
d3 = json.loads(json_str) # 使用loads函数反解序列，并用d2这个变量接收解析出来的这个序列
d4 = json.load(f)
f.close()
print(d4)
print(d2)
print(d3)
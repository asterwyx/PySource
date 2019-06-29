from collections import namedtuple
Point = namedtuple('Point', ['x', 'y']) # 使用namedtuple()方法定义一个新的tuple类型，名为Point，可以看作是tuple的一个子类
p = Point(1,2)
print(p.x)
print(p.y)
print(isinstance(p, tuple))
print(isinstance(p, Point))

# 类似的，可以定义一个圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])
c1 = Circle(1, 2, 3)
print(isinstance(c1, tuple))
print(isinstance(c1, Circle)) # 判断是否是一个圆类

# 双向列表deque
from collections import deque
q = deque([1, 2, 3])
print(q)
q.append(4)
print(q)
q.pop()
print(q)
q.appendleft(8)
print(q)
q.popleft()
print(q)

# 有默认值的defaultedict
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])
# 默认值是调用函数返回的，而函数在创建defaultdict对象时传入

# 有顺序的dict，OrderedDict
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
# 此时的dict是无序的
# 使用OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od) # OrederedDict是按照插入的顺序排序的，并不是按照key本身排序
od2 = OrderedDict()
od2['y'] = 2
od2['z'] = 3
od2['x'] = 1
print(od2)
# OrderedDict可以实现一个FIFO(先进先出)的dict，当容量超出限制时，先删除最早添加的key

from collections import ChainMap
import os, argparse


# 一个逻辑上的dict——ChainMap
# 设置缺省参数

defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

# 组合成Chainmap
combined = ChainMap(command_line_args, os.environ, defaults)


# 打印参数
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

# 一个简单的计数器——Counter
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
# Counter可以说是dict的一个子类

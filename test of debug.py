# 直接打印某一变量查看是否出错
# def foo(s):
#     n = int(s)
#     print(">>>n = %d" % n)
#     return 10 / n


# 断言(assert)来进行调试
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is a zero!'  # 凡是用print来辅助查看的地方，都可以用断言(assert)来替代
#     return 10 / n

# def main():
#     foo('0')

# main()


# 用logging来进行调试
import pdb
import logging
logging.basicConfig(level=logging.INFO)  # 这是logging的配置语句

s = '0'
n = int(s)
n = int(s)
pdb.set_trace()
logging.info('n = %d' % n)  # 此语句用来记录调试信息
print(10 / n)
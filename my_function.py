import math
def  my_abs(x):
    if x > 0:
        return x
    else:
        return -x

def my_square(x):
    return x**2

def quadratic(a,b,c):
    if a == 0:
        print('输入的三个系数不能确定一个一元二次方程\n') 
        if b == 0:
            if c == 0:
                print('方程无效\n')
            else:
                print('方程无解\n')
        else:
            return -c/b
    else:
        delta = b**2 - 4 * a * c
        if delta >= 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            return x1, x2
        else:
            print('方程无实数解\n')
    
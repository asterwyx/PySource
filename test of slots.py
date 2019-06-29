# 用__slots__限制一个实例的可绑定属性
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Cecil'
s.age = 19
print(s.name)
print(s.age)
print('divider.......\n')
# 父类的slots不会限制子类
class GraduateStudent(Student):
    pass

gs = GraduateStudent()
gs.score = 99
print(gs.score)
# 但是假如给子类设置了slots，那么子类的slots应该是父类和子类slots的并集

class IllStudent(Student):
    __slots__ = ('health')

Is = IllStudent()
Is.health = 'good'
print(Is.health)
Is.name = 'Mary'
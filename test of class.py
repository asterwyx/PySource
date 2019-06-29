class Student(object):
    count = 0
    def __init__(self, name, gender):
        Student.count += 1
        self._name = name
        self.__gender = gender
    
    def set_gender(self, gender):
        if gender == 'male':
            self.__gender = 'male'
        elif gender == 'female':
            self.__gender = 'female'
        else:
            raise ValueError('Not gender')
    
    def get_gender(self):
        return self.__gender

bart = Student('Bart', 'male')
mary = Student('Mary', 'female')
if bart.get_gender() != 'male':
    print('测试失败！')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败！')
    else:
        print('测试成功！')
print(Student.count)
print(bart._name)

class Person(object):
    pass


# 给一个实例绑定一个方法
def set_age(self, age):
    self.age = age


import types
s = Person()
s.set_age = types.MethodType(set_age, s)

s.set_age(25)

print(s.age)
# 给class绑定方法
Person.set_age = set_age
p = Person()

p.set_age(35)
print(p.age)
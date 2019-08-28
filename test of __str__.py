# 这是一种定制类的方法
class Student(object):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'Student object (old_name: %s)' %self.name
    __repr__ = __str__ # 此语句让开发人员在命令行调试的时候看到的类打印信息也是和str一样
    

print(Student('Cecil'))
        
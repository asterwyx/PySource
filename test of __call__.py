class Student(object):

    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My old_name is %s' % self.name)

s = Student('Cecil')
s()
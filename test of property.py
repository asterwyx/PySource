class Screen(object):

    @property  # 此修饰器能将一个方法变成对象属性，那么该方法的名字就成了对象属性的名字
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise ValueError('Height must be an int!')
        else:
            self.__height = height
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise ValueError('Width must be an int!')
        else:
            self.__width = width

    @property
    def resolution(self):
        return self.__height * self.__width

s = Screen()
s.height = 1080
s.width = 1920
print(s.height)
print(s.width)
print(s.resolution)
class Polygon:
    __width = None
    __height = None

    def setValue(self, width, height):
        self.__width = width
        self.__height = height

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

class Square(Polygon):
    def area(self):
        return self.getHeight() * self.getWidth()

class Triangle(Polygon):
    def area(self):
        return (self.getWidth()*self.getHeight())/2



s1 = Square()
s1.setValue(9, 12)
print(s1.area())

t1 = Triangle()
t1.setValue(10,20)
print(t1.area())


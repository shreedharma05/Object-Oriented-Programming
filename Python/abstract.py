from abc import ABC, abstractmethod
# use * to import all the classes

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):

    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side

# obj1 = Shape()
obj = Square(4)
print(obj.area())




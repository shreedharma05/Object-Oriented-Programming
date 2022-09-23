class Example:
    def __init__(self):
        self.x = 10
        self._y = 20
        self.__z = 30

    def getValues(self):
        print(self.x)
        print(self._y)
        print(self.__z)
        self.__privateMethod()

    def __privateMethod(self):
        print('private method is executed')


obj = Example()
# print(obj._y)
# print(obj.__z)
obj.getValues()
# obj.__privateMethod()


        
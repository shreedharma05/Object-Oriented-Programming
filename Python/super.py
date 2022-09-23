class Parent:
    def __init__(self):
        print('Parent __init__')

class Parent2:
    def __init__(self):
        print('Parent2 __init__')

class Child(Parent2, Parent):
    def __init__(self):
        print('Child __init__')
        super().__init__()

ch = Child()
print(Child.__mro__) #Method Resolution Order(MRO)

# super() is a built-in allows you to refer parent class by 'super'
# super() is used to call methods from parent class without using parent class's name
# the class which gets inherited first can only use super()
# and the following classes can only be called 
# manually

class Parent:
    def __init__(self):
        print('Parent __init__')

class Child(Parent):
    def __init__(self):
        print('Child __init__')
        Parent.__init__(self)

ch = Child()

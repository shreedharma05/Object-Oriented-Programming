class Python:
    def __init__(self,pages):
        self.pages = pages
        
    # def __init__(self,pages,author):
    #     self.pages = pages    
    #     self.author = author

    def type (self):
        print(self.pages)
        print(self.author)

    def __add__(self, other):
        return self.pages + other.pages

    def __mul__(self, other):
        return self.pages * other.pages

    def __gt__(self, other):
        return self.pages > other.pages

class Java:
    def __init__(self, pages):
        self.pages = pages

b1 = Python(299)
b2 = Python(450,"Arun Venki")
# b1.type()
# b2.type()



# b1 + b2 -> b1.__add__(b2)
print(b1 + b2)
# b1 * b2 -> b1.__mul__(b2)
print(b1 * b2)
# b1 > b2 -> b1.__gt__(b2)
print(b1 > b2)

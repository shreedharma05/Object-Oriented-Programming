class dharma():

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def first(self):
        return self.a + self.b   

class arun(dharma):

    def __init__(self, a, b,c):
        super().__init__(a, b)        
        self.c = c

    def second(self):
        da = dharma.first(self) + self.c 
        return da   

dhyanesh = arun(2,5,8)
print(dhyanesh.second())

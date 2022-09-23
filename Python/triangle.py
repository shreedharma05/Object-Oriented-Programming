from polygon import Polygon as P
from shape import Shape as Sh

class Triangle(P, Sh):
    def area(self):
        return (self.getWidth()*self.getHeight())/2
    
    
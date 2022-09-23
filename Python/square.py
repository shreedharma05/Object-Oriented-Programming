from polygon import Polygon as P
from shape import Shape as Sh

class Square(P, Sh):
    def area(self):
        return self.getHeight() * self.getWidth()
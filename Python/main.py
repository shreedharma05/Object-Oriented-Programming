from square import Square as Sq
from triangle import Triangle as Tr

s1 = Sq()
s1.setValue(9, 12)
s1.setColor('blue')
print('area of square is', s1.area(),'and its color is',s1.getColor())

t1 = Tr()
t1.setValue(10,20)
t1.setColor('green')
print('area of square is', t1.area(),'and its color is',t1.getColor())

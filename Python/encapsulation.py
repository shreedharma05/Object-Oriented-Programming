class Speed:
    def __init__(self):
        self.speed = 10
        self._speed = 20

    def getNewSpeed(self):
        print(self._speed)

    def setNewSpeed(self,newSpeed):
        self._speed = newSpeed

s = Speed()
# s.speed = 50
# print(s.speed)
s._speed = 40
print(s._speed)
# s.getNewSpeed()
# s.setNewSpeed(120)
# s.getNewSpeed()

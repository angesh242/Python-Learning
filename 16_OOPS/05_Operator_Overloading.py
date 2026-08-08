class Point:
    def sum(self,p):
        return Point(self.x + p.x, self.y + p.y)
    def printPoint(self):
        print("x:", self.x, "y:", self.y)
    def __add__(self, p):
        return Point((self.x + p.x), (self.y + p.y))
p1=Point(3,2)
p2=Point(1,4)
p=p1+p2
p.printPoint()
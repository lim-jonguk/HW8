#2번, B835193 석채원
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def move(self,movex,movey):
        self.x += movex
        self.y += movey
        return self
    def __str__(self):
        return '(%d,%d)'%(self.x,self.y)
        
def main() :
     a = Point()
     b = Point(1,5)
     print("a =",a)
     a.move(2,3)
     b.move(4,3).move(-1,-2)
     print("a =",a," B =",b)
main()
    
#2번_B735042_김대겸

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def move(self, z, w):
        self.x += z
        self.y += w
        return self

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

def main():
    a = Point()
    b = Point(1,5)
    print("a =",a)
    a.move(2,3)
    b.move(4,3).move(-1,-2)
    print("a =",a," B =",b)
main()

#1번문제. C111061 박서연. -완료 

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def calArea(self):
        print(self.w * self.h)
    
    def __str__(self):
        return '(%d, %d) %d, %d' %(self.x, self.y, self.w, self.h)
        

def main():
    box1 = Rectangle(0, 0, 100, 100)
    box2 = Rectangle(10, 10, 200, 200)
    print("box: ", box1)
    print("box: ", box2)
    box1.calArea()
    box2.calArea()

main()
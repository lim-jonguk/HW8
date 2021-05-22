#1번_B735042_김대겸

# 사각형을 나타내는 클래스 Rectangle
class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def calArea(self):
        self.calArea = self.w * self.h
        print(self.calArea)  

    def __str__(self):
        return "({},{}) {} {}".format(self.x, self.y, self.w, self.h)   

# main() 함수 선언
def main():
    box1 = Rectangle(0, 0, 100, 100)
    box2 = Rectangle(10, 10, 200, 200)
    print("box: ", box1)
    print("box: ", box2)
    box1.calArea()
    box2.calArea()

main()

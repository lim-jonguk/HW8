#1번 C111152 임종욱

class Rectangle:
    def __init__(self,x,y,w,h):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h     
    def calArea(self):
        Area = self.__w *self.__h
        print(Area)
    def __str__(self):
        return f'({self.__x},{self.__y}) {self.__w},{self.__h}'
   
def main() :
    box1 = Rectangle(0, 0, 100, 100)
    box2 = Rectangle(10, 10, 200, 200)
    print("box: ", box1)
    print("box: ", box2)
    box1.calArea()
    box2.calArea()

main()
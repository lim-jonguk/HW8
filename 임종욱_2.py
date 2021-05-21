#2번 C111152 임종욱

class Point:
    def __init__(self,x =0,y= 0):
        self.__x = x
        self.__y = y
        self.__p = (x,y)
    def move(self,x,y):
        self.__x += x
        self.__y += y
        self.__p = (self.__x,self.__y)
        return self
    def __str__(self):
        return f'{self.__p}'
        
    
def main() :
    a = Point()
    b = Point(1,5)
    print("a =",a)
    a.move(2,3)
    b.move(4,3).move(-1,-2)
    print("a =",a," B =",b)

main()
#7번문제. C111061 박서연. -완료 

class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Complex(x,y)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Complex(x,y)
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return 'Complex('+str(self.x)+','+str(self.y)+')'


def main():
    a = Complex(3.0,-4.5)
    b = Complex(4.0, -5.0)
    c = Complex(-1.0, 0.5)
    print(a+b)
    print(a+b-c)
    print(a-b)
    print(a-b+c)
    print(a-c)
    print(b == (a-c))
    
main()
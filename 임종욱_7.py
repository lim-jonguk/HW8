#7번 C111152 임종욱

class Complex:
    def __init__ (self,a,b):
        self.a = a
        self.b = b
    def __add__(self,other):
        a = self.a + other.a
        b = self.b + other.b
        return Complex(a,b)
    def __sub__(self,other):
        a = self.a - other.a
        b = self.b - other.b
        return Complex(a,b)
    def __eq__(self,other):
        return (self.a == other.a) and (self.b == other.b)
    def __str__(self):
        return f'Complex({self.a},{self.b})'

def main() :
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
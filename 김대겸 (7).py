#7번_B735042_김대겸

class Complex:

    def __init__(self, real, fake): 
        self.real = real
        self.fake = fake
        
    def __add__(self, other):
        return Complex(self.real + other.real, self.fake + other.fake)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.fake - other.fake)
    
    def __eq__(self, other):
        return self.real == other.real and self.fake == other.fake
    
    def __str__(self):
        return '({}, {})'.format(self.real, self.fake)

def main():
    a = Complex(3.0,-4.5)
    b = Complex(4.0,-5.0)
    c = Complex(-1.0,0.5)
    print(a+b)
    print(a+b-c)
    print(a-b)
    print(a-b+c)
    print(a-c)
    print(b == (a-c))
main()

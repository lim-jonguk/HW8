#7번, B835193 석채원
class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
        
    def __add__(self,other):
        x = self.real+other.real
        y = self.imag+other.imag
        return Complex(x,y)
    
    def __sub__(self,other):
        x = self.real-other.real
        y = self.imag-other.imag
        return Complex(x,y)
    
    def __eq__(self,other):
        return self.real == other.real and self.imag == other.imag
    
    def __str__(self):
        return 'Complex('+str(self.real)+','+str(self.imag)+')'
    
def main():
    a = Complex(3.0,-4.5)
    b = Complex(4.0, -5.0)
    c = Complex(-1.0, 0.5)
    print(a+b)
    print(a+b-c)
    print(a-b)
    print(a-b+c)
    print(a-c)
    print(b==(a-c))
main()
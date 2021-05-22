#3번_B735042_김대겸

class Dog:
    def __init__(self, kind, name, trick=''):
        self.kind = kind
        self.name = name
        self.trick = trick

    def add_trick(self, addT):
        self.trick = self.trick + ' ' + addT

    def __str__(self):
        return "{} {}는 {}를 할 수 있습니다.".format(self.kind, self.name, self.trick) 
    
def main():
    a = Dog('월시코기','바둑이')
    b = Dog('푸들','멍멍이')
    a.add_trick('뒹굴기')
    b.add_trick('달리기')
    b.add_trick('점프하기')
    print(a)
    print(b)
main()
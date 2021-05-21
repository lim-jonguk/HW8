#3번 C111152 임종욱

class  Dog:
    def __init__(self,kind,name,tricks= ''):
        self.kind = kind
        self.name= name
        self.tricks = tricks
    def add_trick(self,tricks):
        self.tricks += ' ' + tricks
    def __str__(self):
        return f'{self.kind} {self.name}는 {self.tricks}를 할 수 있습니다'

def main() :
    a = Dog('월시코기','바둑이')
    b = Dog('푸들','멍멍이')
    a.add_trick('뒹굴기')
    b.add_trick('달리기')
    b.add_trick('점프하기')
    print(a)
    print(b)

main()
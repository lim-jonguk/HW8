#3번문제. C111061 박서연. -완료

class Dog:
    allTricks = ''
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name
        self.tricks = Dog.allTricks
    
    def add_trick(self, others):
        self.tricks += ' ' + others
        return self.tricks
        
    def __str__(self):
        return '%s %s는%s를 할 수 있습니다' %(self.kind, self.name, self.tricks)
        
        
def main():
    a = Dog('월시코기','바둑이')
    b = Dog('푸들','멍멍이')
    a.add_trick('뒹굴기')
    b.add_trick('달리기')
    b.add_trick('점프하기')
    print(a)
    print(b)
    
main()
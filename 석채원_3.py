#3번, B835193 석채원
class Dog:
    def __init__(self,kind,name):
        self.kind = kind
        self.name = name
        self.tricklist = list() #객체마다 가지도록 생성자 필드에,클래스 내 메소드가 접근할 수 있도록 인스턴스 변수로
    def add_trick(self,tricks=' '):
        self.tricks = tricks
        (self.tricklist).append(tricks)
    def __str__(self):
        strtricks = str(self.tricklist)[1:-1] #[]제거
        newtricks = strtricks.replace("'","") #'' 제거
        newtricks = newtricks.replace(",","") # ,제거
        return '%s %s는 %s를 할 수 있습니다'%(self.kind,self.name,newtricks)
def main() :
    a = Dog('월시코기','바둑이')
    b = Dog('푸들','멍멍이')
    a.add_trick('뒹굴기')
    b.add_trick('달리기')
    b.add_trick('점프하기')
    print(a)
    print(b)
main()

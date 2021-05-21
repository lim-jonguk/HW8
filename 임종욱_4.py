#4번 C111152 임종욱

class Employee:
    SN = 1
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.sn = Employee.SN
        Employee.SN += 1
    def __str__(self):
        return f'SN : {self.sn} 이름 : {self.name} 월급 : {self.salary}'


def main() :
    a = Employee("사장",1200)
    b = Employee("김수철",300)
    c = Employee("이영애",600)
    print(a)
    print(b)
    print(c)

main()
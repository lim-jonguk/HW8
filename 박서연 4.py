#4번문제. C111061 박서연. -완료 

class Employee:
    number = 0
    
    def __init__(self, name, salary):
        Employee.number += 1
        self.name = name
        self.salary = salary
        self.num = Employee.number
    
    def __str__(self):
        return 'SN : %d 이름 : %s 월급 : %d' %(self.num, self.name, self.salary)


def main():
    a = Employee("사장",1200)
    b = Employee("김수철",300)
    c = Employee("이영애",600)
    
    print(a)
    print(b)
    print(c)
    
main()
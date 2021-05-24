#4번, B835193 석채원
class Employee:
    employeenum = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.employeenum+=1
        self.num = Employee.employeenum
    def __str__(self):
        return 'SN : %d 이름: %s 월급: %s'%(self.num,self.name,self.salary) 
        
def main():
    a = Employee("사장",1200)
    b = Employee("김수철",300)
    c = Employee("이영애",600)
    print(a)
    print(b)
    print(c)
main()
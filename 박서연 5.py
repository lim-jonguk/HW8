#5번문제. C111061 박서연.

class Employee:
    number = 0
    employeeList = []
    
    def __init__(self, name, salary):
        Employee.number += 1
        Employee.employeeList.append(self)
        self.name = name
        self.salary = salary
        self.num = Employee.number
        self.employeeList = Employee.employeeList
        
    
    def __str__(self):
        return 'SN : %d 이름 : %s 월급 : %d' %(self.num, self.name, self.salary)

def main():
    Employee("사장",1200)
    Employee("김수철",300)
    Employee("이영애",600)
    
    for i in Employee("장동철",400).employeeList :
        print(i)

main()
#5번 C111152 임종욱

class Employee:
    SN = 1
    employeeList = []
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.sn = Employee.SN
        Employee.employeeList += [f'SN : {self.sn} 이름 : {self.name} 월급 : {self.salary}']
        Employee.SN += 1
        
    def __str__(self):
        return f'SN : {self.sn} 이름 : {self.name} 월급 : {self.salary}'
    

def main() :
    Employee("사장",1200)
    Employee("김수철",300)
    Employee("이영애",600)
    for i in Employee("장동철",400).employeeList :
        print(i)

main()
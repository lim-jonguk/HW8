#5번_B735042_김대겸

class Employee:
    num = 0
    employeeList = []

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employeeList.append(self)
        
    def __str__(self):
        Employee.num += 1
        
        return "SN : {} 이름 : {} 월급 : {}".format(self.num, self.name, self.salary)


def main():
    a = Employee("사장",1200)
    b = Employee("김수철",300)
    c = Employee("이영애",600)

    for i in Employee("장동철",400).employeeList :
        print(i)

main() 
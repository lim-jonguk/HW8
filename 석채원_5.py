#5번, B835193 석채원
class Employee:
    #클래스 변수들
    employeeList = list()
    employeenum = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.employeenum+=1
        Employee.employeeList.append('SN : %d 이름: %s 월급: %s'%(Employee.employeenum,self.name,self.salary))


def main() :
    Employee("사장",1200)
    Employee("김수철",300)
    Employee("이영애",600)
    for i in Employee("장동철",400).employeeList :
       print(i)
main()

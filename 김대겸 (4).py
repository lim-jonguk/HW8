#4번_B735042_김대겸

class Employee:
    num = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def __str__(self):
        Employee.num += 1
        return "SN : {} 이름 : {} 월급 : {}".format(self.num, self.name, self.salary)   

def main():
    a = Employee("사장",1200)
    b = Employee("김수철",300)
    c = Employee("이영애",600)

    print(a) 
    print(b) 
    print(c)

main() 
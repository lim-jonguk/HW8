#6번, B835193 석채원
class BankAccount:
    interest_rate = 0.3
    def __init__(self,name,num,balance):
        self.name = name
        self.num = num
        self.balance = balance
    def deposit(self,number1):
        self.balance += number1
    def withdraw(self,number2):
        self.balance-=number2
        
    def maturityAmount(self):
        maturity = self.balance*(1+BankAccount.interest_rate)
        return maturity
    
    def __str__(self):
        return 'name:%s Number: %s Balance: %d'%(self.name,self.num,self.balance)
    
def main():
    a = BankAccount("김철수","82345",1000)
    print(a)
    print("Interest Rate =",BankAccount.interest_rate,"Maturity : ", a.maturityAmount())
    a.deposit(3000)
    print(a)
    a.withdraw(1500)
    print(a)
    BankAccount.interest_rate = 0.7
    print("Interest Rate =", BankAccount.interest_rate, 
    "Maturity : ", a.maturityAmount())
main()

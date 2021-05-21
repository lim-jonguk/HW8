#6번 C111152 임종욱

class BankAccount:
    interest_rate = 0.3
    def __init__(self,name,Number,Balance):
        self.name = name
        self.Number = Number
        self.Balance = Balance
    def __str__(self):
        return f'Name:{self.name} Number : {self.Number} Balance : {self.Balance}'
    def deposit(self,B):
        self.Balance += B
    def withdraw(self,B):
        self.Balance -= B
    def maturityAmount(self):
        return f'{self.Balance *(1+ BankAccount.interest_rate)}'

        
        

def main() :
    a = BankAccount("김철수","82345",1000)
    print(a)
    print("Interest Rate =",BankAccount.interest_rate,
            "Maturity : ", a.maturityAmount())
    a.deposit(3000)
    print(a)
    a.withdraw(1500)
    print(a)
    BankAccount.interest_rate = 0.7
    print("Interest Rate =", BankAccount.interest_rate,
            "Maturity : ", a.maturityAmount())

main()
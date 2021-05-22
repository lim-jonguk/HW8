#6번_B735042_김대겸

class BankAccount:
    interest_rate = 0.3
    
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def maturityAmount(self): # 만기일때의 금액
        return self.balance + (self.balance * BankAccount.interest_rate)

    def __str__(self): # 출력
        return "Name:{} Number:{} Balance:{}".format(self.name, self.number, self.balance)

    def deposit(self, depo_am): # 입금
        self.balance += depo_am

    def withdraw(self, with_am): # 출금
        self.balance -= with_am


def main():
    a = BankAccount("김철수","82345",1000)
    print(a)
    print("Interest Rate =",BankAccount.interest_rate,
        "Maturity : ", a.maturityAmount())
    a.deposit(3000)
    print(a)
    a.withdraw(1500)
    print(a)
    BankAccount.interest_rate = 0.7
    print("Interest Rate =",BankAccount.interest_rate,
        "Maturity : ", a.maturityAmount())
main()
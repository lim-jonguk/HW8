#6번문제. C111061 박서연. -완료 

class BankAccount:
    interest_rate = 0.3
    
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
        
    def maturityAmount(self):
        maturity = self.balance * (1 + BankAccount.interest_rate)
        return maturity
        
    def __str__(self):
        return "Name:%s Number: %s Balance: %d" %(self.name, self.number, self.balance)


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
    print("Interest Rate =", BankAccount.interest_rate,
          "Maturity : ", a.maturityAmount())
    
main()
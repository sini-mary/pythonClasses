class Account:
    bankAcc="Equity"
    def __init__(self,balance,accNumber,userName) :
        self.balance=balance
        self.accNumber=accNumber
        self.userName=userName
        
        
    def withdraw(self,amount):
        withdrawals={self.balance}-amount
        return withdrawals
    
    def deposit(self,amount):
        newbalance={self.balance}+amount
        return newbalance
        
     
        
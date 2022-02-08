class Account:
    def __init__(self,acount_number,account_holder,opening_balance):
        self.acount_number=acount_number
        self.account_holder=account_holder
        self.opening_balance=opening_balance

    def __str__(self):
        return 'Account['+self.acount_number+']'+' - '+self.account_holder+' - balance = '+str(self.opening_balance)
    
    def deposite(self,number_of_deposite):
        balance=self.opening_balance+number_of_deposite
        self.curent_balance=balance
    
    def withdraw(self,number_of_withdraw):
        balance=self.curent_balance-number_of_withdraw
        self.curent_balance=balance

    def get_balance(self):
        current_balance=self.curent_balance
        return current_balance

class Current_acount(Account):
    def __init__(self,acount_number,account_holder,opening_balance,
                    overdraft_limit):
                    super().__init__(acount_number,account_holder,opening_balance)
                    self.overdraft_limit=overdraft_limit
    def __str__(self):
        return super().__str__()+', overdraft_limit: '+str(self.overdraft_limit)

    def withdraw(self,number_of_withdraw):
        balance=self.curent_balance
        if number_of_withdraw>=self.overdraft_limit:
            print("Withdrawal would exceed your overdraft limit")
            balance=balance
        else:
            balance=self.curent_balance-number_of_withdraw
        self.curent_balance=balance

class DepositeAccount(Account):
    def __init__(self,acount_number,account_holder,opening_balance,interest_rate):
        super().__init__(acount_number,account_holder,opening_balance)
        self.interest_rate=interest_rate
    def __str__(self):
        return 'Deposite '+super().__str__()+', interest_rate: '+str(self.interest_rate)

class InvestmentAccount(Account):
    def __init__(self,acount_number,account_holder,opening_balance,investment_type):
        super().__init__(acount_number,account_holder,opening_balance)
        self.investment_type=investment_type
    def __str__(self):
        return 'Investment '+super().__str__()+', Investment type: '+self.investment_type


acc1=Current_acount('123','John',10.05,100.0)
print(acc1)
acc2=DepositeAccount('345','John',23.55,0.5)
print(acc2)
acc3=InvestmentAccount('567','Mario',12.45,'high risk')
print(acc3)


acc1.deposite(23.45)
acc1.withdraw(12.33)
print('balance:',acc1.get_balance())

acc1.withdraw(300.00)
print('balance:',acc1.get_balance())


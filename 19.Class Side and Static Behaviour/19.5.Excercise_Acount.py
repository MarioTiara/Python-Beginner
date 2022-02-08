class Account:
    instance_count=0
    @classmethod
    def increamnet_instance_count(cls):
        cls.instance_count+=1
    @staticmethod
    def mesaage():
        print("An instance created")

    def __init__(self,number,name,opening_balance,acount_type):
        Account.mesaage()
        Account.increamnet_instance_count()
        self.number=number
        self.name=name
        self.opening_balance=opening_balance
        self.acount_type=acount_type

    def __str__(self):
        return 'Account['+self.number+']'+' - '+self.name+', '+self.acount_type+' account = '+str(self.opening_balance)
    
    def deposite(self,number_of_deposite):
        balance=self.opening_balance+number_of_deposite
        self.curent_balance=balance
    
    def withdraw(self,number_of_withdraw):
        balance=self.curent_balance-number_of_withdraw
        self.curent_balance=balance

    def get_balance(self):
        curent_balance=self.curent_balance
        return curent_balance

acc1=Account('123','Mario',10.05,'current')
acc2=Account('345','Mario',23.55,'savings')
acc3=Account('567','Tiara',12.45,'investment')

print('Number of Account instances created:',Account.instance_count)
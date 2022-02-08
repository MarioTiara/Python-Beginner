class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return self.name+' is '+str(self.age)
    def birthday(self):
        print('Happy birthday you were ',self.age)
        self.age+=1
        print('You are now', self.age)
    def calculate_pay(self,hours_worked):
        rate_of_pay=7.50
        if self.age>=21:
            rate_of_pay+=2.50
        return hours_worked*rate_of_pay
    def is_teeneger(self):
        return self.age<20
        




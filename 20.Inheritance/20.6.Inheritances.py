class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return self.name+" is "+str(self.age)
    def birthday(self):
        print('Happy Birthday yout were',self.age)
        self.age+=1
        print('You are now ', self.age)

class Employee(Person):
    def __init__(self,name,age,id):
        super().__init__(name,age)
        self.id=id
    def calculate_pay(self,hours_worked):
        rate_of_pay=7.50
        if self.age>=21:
            rate_of_pay+=2.50
        return hours_worked*rate_of_pay

class SalesPerson(Employee):
    def __init__(self,name,age,id,region,sales):
        super().__init__(name,age,id)
        self.region=region
        self.sales=sales
    def bonus(self):
        return self.sales*0.5


print('Person')
p=Person('Mario',23)
print(p)
print("-"*35)

e=Employee('Tiara',30,7468)
print('Employe:',e.name)
e.birthday()
print(e.name+'.calculate_pay(40)',e.calculate_pay(40))
print('-'*35)

s=SalesPerson('Pratama',21,4712,'UK',30000.0)
print('Sales Person: ',s.name)
s.birthday()
print(s.name,'.calculate_pay(40):',s.calculate_pay(40))
print(s.name,'.bonus():',s.bonus())
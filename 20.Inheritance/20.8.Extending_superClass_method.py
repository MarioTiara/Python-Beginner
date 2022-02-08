class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
       return self.name + ' is ' + str(self.age)
    


class Employee(Person):
    def __init__(self,name,age,id):
        super().__init__(name,age)
        self.id=id
    def __str__(self):
        return super().__str__()+" - id("+str(self.id)+")"



p=Person('John',54)
print(p)
e=Employee('Denise',51,1234)
print(e)
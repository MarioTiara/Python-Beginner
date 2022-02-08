class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
       return self.name + ' is ' + str(self.age)
    @staticmethod
    def _A():
        print ("M")


class Employee(Person):
    def __init__(self,name,age,id):
        super().__init__(name,age)
        self.id=id
    def __str__(self):
        return super().__str__()+" - id("+str(self.id)+")"



p=Person('John',54)
print(p)
p.__A()
e=Employee('MArio',23,123)
#e._A()
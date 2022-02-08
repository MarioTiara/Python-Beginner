class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return self.name+' is '+str(self.age)
    def getter(self):
        return self.name+' is '+str(self.age)


p1=Person('Mario',23)
print('P1:',p1)
print('P1.getter:',p1.getter())
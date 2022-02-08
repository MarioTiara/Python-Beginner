class Person:
    instance_count=0
    def __init__(self,name,age):
        Person.instance_count+=1
        self.name=name
        self.age=age
        
p1=Person('Jason',36)
p2=Person('carol',21)
p3=Person('James',19)
print(Person.instance_count)
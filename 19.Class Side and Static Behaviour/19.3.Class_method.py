class Person:
    instance_count=0
    @classmethod
    def increamnet_instance_count(cls):
       cls.instance_count+=1

    def __init__(self,name,age):
        Person.increamnet_instance_count() #can involved in class self
        self.name=name
        self.age=age

p1=Person("mario",23)    
print(Person.instance_count)





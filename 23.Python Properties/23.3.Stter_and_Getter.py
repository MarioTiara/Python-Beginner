class Person:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def get_age(self):
        return self._age
    def set_age(self,new_age):
        if (isinstance(new_age,int) and new_age>0 and new_age<120):
            self._age=new_age
        else:
            self._age=self._age
    def get_name(self):
        return self._name
    def __str__(self):
        return 'Personal['+str(self._name)+'] is ' + str(self._age)



person=Person('John',54)
print(person._age)
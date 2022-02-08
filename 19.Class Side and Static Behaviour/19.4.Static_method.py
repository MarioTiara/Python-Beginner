class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @staticmethod
    def BMI(heigh,weight):
        heigh=heigh/100
        return weight/(heigh*heigh)

p1=Person('Mario',23)
print(p1.name,' is ',p1.age,', BMI :',Person.BMI(163,52))
p2=Person('Tiara',10)
print(p2.name,' is ', p2.age, ', BMI :',Person.BMI(110,29))

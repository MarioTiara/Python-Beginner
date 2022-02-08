class Quantity:
    def __init__(self,value=0):
        self.value=value
    def __add__(self,other):
        new_value=self.value+other.value
        return (Quantity(new_value))
    def __sub__(self,other):
        new_value=self.value-other.value
        return Quantity(new_value)
    def __str__(self):
        return 'Quantity['+str(self.value)+']'

q1=Quantity(9)
q2=Quantity(10)
print(q1,',',q2)
q3=q1-q2
print(q3)
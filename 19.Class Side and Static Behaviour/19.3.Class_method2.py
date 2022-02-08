class Person:
    def __init__(self,gelar=""):
        self.name="Mario"
        self.age=23
        self.gelar=gelar
    
    @classmethod
    def Gelar(cls):
        gelar=",S.T"
        extra=cls(gelar)
        res=extra.name+extra.gelar
        return res

print(Person.Gelar())
        

    





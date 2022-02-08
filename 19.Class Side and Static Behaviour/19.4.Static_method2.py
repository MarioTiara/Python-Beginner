class Person:
    @staticmethod
    def static_function():
        print('hello')
    def __init__(self):
        Person.static_function()
p1=Person()
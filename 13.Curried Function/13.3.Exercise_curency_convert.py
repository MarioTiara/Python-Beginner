def Convert(a,b):
    return a*b

def curry(func,rate):
    def fungsi(y):
        return func(rate,y)
    return fungsi

dollars_to_sterling=curry(Convert,0.77)
print(dollars_to_sterling(5))

euro_to_sterling=curry(Convert,0.88)
print(euro_to_sterling(15))

sterling_to_dollars=curry(Convert,1.3)
print(sterling_to_dollars(7))

sterling_to_euro=curry(Convert,1.14)
print(sterling_to_euro(9))
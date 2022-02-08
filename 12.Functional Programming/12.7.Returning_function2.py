def make_funtion(s):
    if s=='add':
        def adder(x,y):
            return x+y
        return adder
    elif s=='subs':
        def substarct(x,y):
            return x-y
        return substarct
    elif s=='mult':
        def multiply(x,y):
            return x*y
        return multiply
    else:
        raise ValueError('Unkown request')
    
f1=make_funtion('add')
f2=make_funtion('subs')
f3=make_funtion('mult')

print(f1(3,2))
print(f2(3,2))
print(f3(3,2))
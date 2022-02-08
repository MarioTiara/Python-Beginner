def multiply(a,b):
    return a*b

def multby(func,num):
    return lambda y:func(num,y)

double=multby(multiply,2)
print(double(5))
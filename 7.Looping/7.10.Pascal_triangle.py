def fact(num):
    faktorial=1
    if num<=1:
        return 1
    elif num==2:
        return 2
    else:
        for i in range (1,num+1):
            faktorial=faktorial*i
        return faktorial

n=int(input("Enter number of rows:"))
for i in range(n):
    for j in range (n-i-1):
        print(end=" ")
    for j in range (i+1):
        print(fact(i)//(fact(j)*fact(i-j)), end=" ") 
    print()

"""
i=3
for j in range(i+1):
    print(fact(i)//(fact(j)*fact(i-j)), end=" ") 
"""
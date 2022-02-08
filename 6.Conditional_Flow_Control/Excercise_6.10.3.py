'''
We will add several new tests to your program:
1. Modify your program such that it verify that the user has entered a positivedistance (i.e. they cannot enter a negative number).
2. Now modify your program to verify that the input is a number; if it is not anumber then do nothing; otherwise convert the distance to miles.
'''

Distance=input("Input Distance:")
if int(Distance)>0:
    if Distance.isnumeric()==True:
        Distance2=int(Distance)*0.621371
        print(Distance, " Km =", Distance2, "Miles")
    else:
        print("You had entered thing not numeric")
else:
    print("You can't Enter negative value")
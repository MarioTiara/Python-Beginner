num=int(input("Enter a number:"))
def fact(number):
    faktorial=1
    if number<0:
        print("The factorial is not defined")
    elif number==0:
        print("0! =", faktorial)
    else:
        for i in range(1,number+1):
            faktorial=faktorial*i
        print(number,"! = ",faktorial)


fact(num)
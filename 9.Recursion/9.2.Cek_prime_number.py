def is_prime(number,a=2):
    prime=True
    if a>=number:
        print("",end='')
    elif(number%a)==0:
        prime=False
    else:
        return is_prime(number,a+1)
    return prime

num=int(input("Enter a integer number:"))
print('is_prime(',num,')',is_prime(num))
    

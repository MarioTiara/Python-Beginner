#check Input Is posiitvie or Negative
'''
1. Prompt the user to input a number (use the input() function). You can assumethat the input will be some sort of number.
2. Convert the string into an integer using the int() function.
3. Now check whether the integer is a positive number or a negative number.
4. You could also add a test to see if the number is Zero.
'''

number=int(input("Enter a Number:"))
if number>0:
    print("Number is Postitive")
elif number<0:
    print("Number is Negative")
else:
    print("Number is Zero")
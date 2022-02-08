name=input("enter your name:")

if len(name)>15:
    print("your name consist of",len(name),"character,its so long")
elif len(name)<1:
    print("you have not enter your name")
else:
    print("Congratulation")
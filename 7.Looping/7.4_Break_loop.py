print('only print code if all iterations completed')
num= int(input('Enter a number to check for:'))
for i in range(0,6):
    if i==num:
        break
    print(i,' ',end='')
print('Done')
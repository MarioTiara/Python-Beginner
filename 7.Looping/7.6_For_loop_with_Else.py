#only print cide if all iterations completed over a list

print('Only print code if all iterations completed')

num=int(input('Enter a number to check for:'))
for i in range(0,6):
    if i==num:
        break
    print(i, ' ', end='')
else:
    print()
    print('All iterations succesful')
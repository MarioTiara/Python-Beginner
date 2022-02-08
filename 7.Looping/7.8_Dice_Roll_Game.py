import random
MIN=1
MAX=6

roll_again='y'

while roll_again=='y':
    print('Rolling the dices..')
    print('The values are..')
    dicel1=random.randint(MIN,MAX)
    print(dicel1)
    dicel2=random.randint(MIN,MAX)
    print(dicel2)
    roll_again=input('Roll the dices again? (y/n :')
    


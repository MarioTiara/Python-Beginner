import random
print("welcome to the number guess game")
number_to_guess=random.randint(1,10)
count_number_of_tries=1

guess=int(input("Pleae guess a number between 1 and 10:"))

while number_to_guess!=guess:
    print("Sory wrong number")
    if guess<number_to_guess:
        print("your guess was lower than the number")
    else:
        print("your guess was higher than the number")
    if count_number_of_tries==4:
        break
    guess=int(input('Please guess again:'))
    count_number_of_tries+=1

if number_to_guess==guess:
    print('well done you won!')
    print('you took',count_number_of_tries, 'goues to complete the game')
else:
    print("sory - you loose")
    print('the number you needed to guess was', number_to_guess)
print('Game Over')
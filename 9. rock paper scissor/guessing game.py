import random
import os

play = 'y'
while play == 'y':
    os.system('cls')
    num = random.randint(1, 50)
    print('Welcome to number guessing game!!')
    print('Guess a number between 1 to 99')
    for i in range(10):
        if i == 5:
            print(f'\nOpps you ran out of guesses! The number was {num}')
            break
        guess = int(input(f'You have {5 - i} guesses remaing:'))
        if num == guess:
            print(f'Hurra! Your Guess number of {num} was right\n')
            break
        elif guess > num:
            print('TOO HIGH!')
        else:
            print('TOO LOW!')
    play = input('Do you want to play again? (y/n): ')
print('Thanks for playing, Bye!')

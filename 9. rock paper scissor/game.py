import random
import os

pscore = 0
cscore = 0
play = 'y'
while play == 'y':
    os.system('cls')
    print('................Rock................')
    print('................Paper...............')
    print('................Scissor.............')
    print('Welcome to rock paper scissor game!!')
    print()
    choice = input('Make your Move: ').lower()
    c = ['rock', 'paper', 'scissor']
    num = random.randint(0, 2)

    if choice in c:
        print(f'Computer plays: {c[num]}')
        if choice.lower() == c[num]:
            print('Its a Tie!')
        elif choice == 'rock' and c[num] == 'scissor':
            print('You won!')
            pscore += 1
        elif choice == 'paper' and c[num] == 'rock':
            print('You won!')
            pscore += 1
        elif choice == 'scissor' and c[num] == 'paper':
            print('You won!')
            pscore += 1
        else:
            print('Computer Wins!')
            cscore += 1
    else:
        os.system('cls')
        userinput = input(
            'something went wrong! Please make correct move!\nNow Enter any key to continue or q to exit: ').lower()

        if userinput == 'q':
            os.system('cls')
            exit()
        else:
            continue
    print(f'\nYour Score: {pscore}     Computers score: {cscore}')
    play = input('Do yo want to play again? (y/n): ')

os.system('cls')  # to clear screen

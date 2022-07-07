user_response = None
chance = 0
while user_response != 'please':
    print(f'You have {3 - chance} Chances left')
    user_response = input('Say the magic word to get into Hogworts: ').lower()
    chance += 1
    if chance >= 3:
        print('You have no Chances left, so Fuck Off')
        print('And You are not welcomed at Hogworts')
        exit()
print('Welcome to Hogworts')

# exit() exits the entire code itself, not just loop
# break exits the loop only
# Continue is used to skip particular loop


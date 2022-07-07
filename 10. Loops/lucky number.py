for i in range(1,21):
    if i==4 or i==13:
        state='UNLUCKY!'
    elif i%2==0:
        state='Even'
    else:
        state='Odd'
    print(f"{i} is {state}")

    
"""
for i in range(1,21):
    if i==4 or i==13:
        print(f"{i} is UNLUCKY!")
    elif i%2==0:
        print(f'{i} is Even')
    else:
        print(f'{i} is Odd')
"""
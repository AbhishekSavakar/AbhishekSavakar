kms=int(input('How many kilometers did you run today: '))
print(f'You said {kms}km which is {round(kms*0.621371,2)}mi')

'''
round(thing to round, how many places)
print('hi'+ round(kms*0.621371,2))
TypeError: can only concatenate str (not "float") to str
'''

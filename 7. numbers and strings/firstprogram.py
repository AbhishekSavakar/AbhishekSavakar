print('Hello')
print(type(5))  # Type of data

# Order of execution PEMDAS
# parenthesis, Exponential, Multiplication, Division, Addition, Subtraction
print(2 ** 3)  # Exponential
print(2 * 5)  # Multiplication
print(7 / 3)  # Division
print(2 + 3)  # addition
print(3 - 2)  # subtraction
print(7 // 3)  # Integer Division

'''
Naming restrictions
# 1. Variable must start with letters or underscore
# 2. The rest of the name must consist of letters, numbers or underscores
# 3. Names are case-sensitive

Naming conventions
# camelCase snake_case
# Python uses snake_case(separated by underscore not capital letters to separate words)
# Expect UpperCamelCase usually refers to a class
'''

'''
\n to print on new line
'''

string1 = 'Abhishek'
string2 = 'Savakar'
print(string1 + string2)
print(string1, string2)

print('My name is' + ' ' + string1 + ' ' + string2)
print('My name is', string1, string2)
print('My name is {} {}'.format(string1, string2))
# We will use
print(f'My name is {string1} {string2}')

print(string1[0])
print(string1[0:])
# [start:stop:step]
print(string1[::-1])

name=input('Enter your name')
# input() always takes data type as string


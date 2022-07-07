nums = list(range(1, 10))

print(f'Even number:{[n for n in nums if n % 2 == 0]}')
print(f'Odd number:{[n for n in nums if n % 2 != 0]}')
print(f'numbers:{[n * 2 if n % 2 == 0 else n / 2 for n in nums]}')
# if true execute left side else right
sentance = 'if true execute left side else right'
print([char for char in sentance if char not in 'aeiou '])
print(''.join([char for char in sentance if char not in 'aeiou ']))
print(''.join([char for char in sentance if char not in 'aeiou']))

# Nested list
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[z for z in x] for x in a]
# print(b)
# print([[print(z) for z in x] for x in a])
print(a)
print(len(a))
print(a[1][1])
board=[[num for num in range(1,9)] for val in range(1,2)]
print(board)

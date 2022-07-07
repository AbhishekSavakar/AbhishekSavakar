# [__for__in__]
# Used, whenyou want to create a list from existing list

# nums=list(range(4))
# y=[x*10 for x in nums]
y=[x*10 for x in range(4)]
print(y)
print(type(y))

a=[bool(val) for val in [0,[],'']]
print(a)
b=[str(nums) for nums in range(1,4)]
print(b)
print([num for num in range(10)])
print(f'Even numbers: {[num for num in range(10) if num%2==0]}')
print(f'Odd numbers: {[num for num in range(10) if num%2!=0]}')

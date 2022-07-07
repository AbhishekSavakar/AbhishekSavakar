cat1 = {'cat': "sunny", 'dog': 'bidhu'}
cat2 = dict(cat='kitty')
# cat is written without ''
print(cat1)

print(cat1['cat'])

for val in cat1:
    print(val)
for v in cat1.values():
    print(v)
for k in cat1.keys():
    print(k)
for k, v in cat1.items():
    print(k, v)
# order is not gaureented in dict

if 'cat' in cat1.keys():
    print('vola')
else:
    cat1['cat'] = 'kittyy'

cat2.clear()
print(cat2)
cat2 = cat1.copy()
print(cat2)
# Create a new dictionary with keys from iterable
# and values set to value.
cat2 = {}.fromkeys(['name', 'age', 'email', 'phone'], None)
# {'name': None, 'age': None, 'email': None, 'phone': None}
print(cat2)
print(cat1.get('cat'))
print(cat1.get('pet'))
# .get method gets value if present else none

cat3={'address':None}
cat3.update(cat2)
print(cat3)

# updates extendes first list to second or updates certain value
# cat3={'address':'None'} wrong way to update certain value in dict.
cat3['address']='Gandhi Galli'
print(cat3)

cat3.pop('address')
print(cat3)

cat3.popitem()
print(cat3)
# popitem removes randomly some item
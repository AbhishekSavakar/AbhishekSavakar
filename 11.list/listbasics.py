profile = ['AWS Developer', 'Python Developer', 'Web Developer', 'ML Engineer', 'Blockchain Developer']
print(profile)
print(len(profile))
tasks = list(range(10))
print(tasks)
print(profile[0])
print(profile[:])

for i in profile:
    print(i)

for i,role in enumerate(profile):
    print(i+1,role)
profile.sort()
print(profile)
profile.append([2,3])
print(profile)
profile.extend([2,3])
print(profile)
profile.insert(5,1)
print(profile)
profile.remove(3)#value remove
print(profile.index(2))#to find index of value
print(profile[profile.index(2)]) #to print value of particular index
# profile.clear()
print(profile)
profile.pop()#to remove items from index, default last one.
print(profile)
profile.remove(1) #to remove item using value.
print(profile)

"""
if we know index we can find value using profile[index]=value
if we know value we can find its index using profile.index(value)=index
to remove using index use .pop(index)
to remove using value use .remove(value)

"""
l=[1,2,3,1,2,1,2,1,1]
print(l.count(1))
l.reverse()
print(l)

profile = ['AWS Developer', 'Python Developer', 'Web Developer', 'ML Engineer', 'Blockchain Developer']
print(profile[::-1])
print(profile)
str=' '.join(profile)# it works only when list contains string
print(' '.join(profile))
print(str)
print(str.split('Developer '))

# join is used LIST=>STRING
#split is use STRING=>LIST

"""
if you want to add one element use=append
more than one item use extend
insert(where,what)
"""

print(profile)
profile[3]='ML Developer'
print(profile)

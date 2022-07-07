playlist={
    'title':'New In EDM',
    'author':'Wynk music',
    'songs':[
    {'name':'Somebody Like U' ,'singer':'Alan Walker', 'album':'Walkerverse','duration':4.2},
    {'name':'Do It Better' ,'singer':'Felix Jaehn', 'album':'Do It Better','duration':3.2},
    {'name':'Caught Up' ,'singer':'Gryffin', 'album':' Darkroom','duration':2.1}
]
}
# print(playlist.get('songs'))
# print(playlist.keys())
print(type(playlist.get('songs')))
newsongs=['perfect','Caught Up','samajavargavana']
# for j in newsongs:
#     for i in playlist.get('songs'):
#         if j not in i.values():
#
#             # # print(type(i),type(j))
#             # playlist['songs'].append(i)
print(playlist)
# for i in newsongs:
#     if i not in playlist.get('songs'.keys()):


sqnum={num:num*num for num in range(1,21)}
print(sqnum)
cubenum={key:value*key for key,value in sqnum.items()}
print(cubenum)
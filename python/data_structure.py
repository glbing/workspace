#!/usr/bin/env python
# coding=utf-8
'''shoplist=['apple','banana','mango','carrot',6]
print(len(shoplist))
for item in shoplist:
    print item
shoplist.append('rice')
print(shoplist)
shoplist.sort()
print(shoplist)
print(shoplist[2])
del shoplist[3]
print(shoplist)
shoplist.reverse()
print(shoplist)
shoplist.insert(2,'hgf')
print(shoplist)'''
'''
zoo=(1,2,3)
print(zoo)
newzoo=(zoo,2,3,zoo,4,3,9)
print(newzoo[3][2])

print((1,23,4))
tuble=(12,['dede','ded'])
print(tuble)
'''
#
ab={
    'glb':'13929518646',
    'dzs':'13978444851',
    'll': '14789259994'
}
print(ab)
print(ab['glb'])
ab['cgy']='458555959'
del ab['ll']
print(ab)
for name,telephone in ab.items():
    print(name,telephone)
if 'glb' in ab:
    print('cunzai')
list=[1,2,3,4,4]
if 92 not in list:
    print('cunzaiq')
ab['num']=list
print(ab)
ab['num'].remove(3)
print(ab)
print(ab.items())

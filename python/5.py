#!/usr/bin/env python
# coding=utf-8
'''f=open("test.txt",'w')
buf="dedhuhuijijijijijijdidjijdijidejdjidjiji\n"
print(f.tell())
f.seek(f.write(buf),0)
f.write(buf)
f.write(buf)
f.close()

import pickle 
list=[1,2,3,4,7]
f=open("test1.dat",'wb')
pickle.dump(list,f)
f.close()
del list
f=open("test1.dat",'rb')
list1=pickle.load(f)
f.close()
print(list1)
f=open('test.txt','a')
f.write("ddd\nwwwx k")
f.close()'''

f=open("test.txt",'w')
f.write("ededdeded")
f.close()

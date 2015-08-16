#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
def fun(x):
    return int(x) 
fd=open("/home/dji/work11/data.txt")
print fd
data=[]
for lines in fd.readlines():
    lines=lines.strip("\n")
    lines=lines.split()
    #print (lines)
    #lines=map(int,lines)
    data=data+lines

for i in range(len(data)-1):
    data[i]=float(data[i])
    print data[i]
x1=np.array(range(len(data)))
print(len(x1))
y1=np.array(data)
print(len(y1))
for i in range(1):
    plt.plot(x1,y1,"r")
plt.show()
fd.close()

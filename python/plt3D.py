#!/usr/bin/env python
# coding=utf-8

from  mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x =[0,2,3,4,5,6,7,8,9,10]
y =[0,6,2,3,13,4,1,2,4,8]
z =[0,3,3,3,5,7,9,11,9,10]



ax.plot(x, y, z,label='parametric curve')
ax.legend()
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

#!/usr/bin/env python
# coding=utf-8
#import operator
from numpy import *#*代表将numpy全部导入
import sys
import matplotlib.pyplot as plt
def create_dataset():
    group=array([[1.0,1],[1.0,0],[0,0],[0,0.1]])
    label=['A','A','B','B']
    return group,label
'''group,label=create_dataset()#三个引号
print group, label
'''
#s6 = 'I realy like "python"!'
#print s6
"""if __name__=="__main__":
    print "123"
else:
    print "456"
"""
dataset,labels=create_dataset()
def classify0(inx,k):
    datasetsize=dataset.shape[0]
   # print datasetsize

    diffmat=tile(inx,(datasetsize,1))-dataset
   # print diffmat
   # print dataset
    sq_diffmat=diffmat**2
   # print sq_diffmat
    sq_diatance=sq_diffmat.sum(axis=1)
   # print sq_diatance
    diatance=sq_diatance**0.5
    sorted_distance_indicies=diatance.argsort()
   # print sorted_distance_indicies
    classcout={}
    k=int(k)
    for i in range(k):
        votelabel=labels[sorted_distance_indicies[i]]
        #print votelabel
        classcout[votelabel]=classcout.get(votelabel,0)+1
   # print classcout
    temp=classcout.items()
    a=sorted(temp,key=lambda temp:temp[1],reverse=True)
    print a
    return a[0][0]
'''f __name__=="__main__":
    if len(sys.argv)!=2:
        print "input error"
    else:
        print classify0([-5,-7],sys.argv[1])
'''
def file_matrix(filename):
    fr=open(filename)
    array_lines_list=fr.readlines()
    #print array_lines_list
    num_lines=len(array_lines_list)
    #print num_lines
    mat=zeros([num_lines,3])
    label_vector=[]
    index=0
    for line in array_lines_list:
        line=line.strip()#str
        temp=line.split()#list
        mat[index:]=temp[0:3]
        label_vector.append(temp[-1])
        index +=1
   # print mat
   # print len(label_vector)
    return mat,label_vector
mat,label=file_matrix("datingTestSet.txt") 
for i in range(len(label)):
    if label[i] == "largeDoses":
        label[i]=int(1)
    elif label[i] =="smallDoses":
        label[i]=int(2)
    else:
        label[i]=int(3)
label=array(label)
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_title("dataset")
ax.scatter(mat[:,0],mat[:,1],15*label,15*label)
plt.show()





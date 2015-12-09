#!/usr/bin/env python
# coding=utf-8
#import operator
from numpy import *#*代表将numpy全部导入
#import sys
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
#dataset,labels=create_dataset()
def classify0(inx,dataset,labels,k):
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
    #print a
    return a[0][0]
'''if __name__=="__main__":
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
#mat,label=file_matrix("datingTestSet.txt") 


def autonorm(mat_list):
    #dataset=mat_list[0]
    colum_min=mat_list[0].min(0)
    colum_max=mat_list[0].max(0)
    colum_min1=tile(colum_min,(mat_list[0].shape[0],1))
    colum_max1=tile(colum_max,(mat_list[0].shape[0],1))
    range=colum_max1-colum_min1
    mat_list[0]=(mat_list[0]-colum_min1)/range
   # return dataset
#print mat



def knn_test():
    ratio=0.1
    datamat,labels=file_matrix("datingTestSet.txt")
    for i in range(len(labels)):
        if labels[i] == "largeDoses":
            labels[i]=int(1)
        elif labels[i] =="smallDoses":
            labels[i]=int(2)
        else:
            labels[i]=int(3)
    mat_list=[]
    mat_list.append(datamat)
    autonorm(mat_list)
    mat=mat_list[0]
    labels=array(labels)

    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.set_title("dataset")
    ax.scatter(mat[:,0],mat[:,1],15*labels,15*labels)
    plt.show()

    total_num=mat.shape[0]
    test_num=int(total_num*ratio)
    j=0
    for i in range(test_num):
        result=classify0(mat[i,:],mat[test_num:total_num,:],labels[test_num:total_num],7)
        if result == labels[i]:
            j += 1.0
            print (str(result)+ " "+ str(labels[i]))
    print (j/float(test_num))

if __name__ == "__main__":
    knn_test()




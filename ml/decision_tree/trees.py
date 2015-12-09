#!/usr/bin/env python
# coding=utf-8
from math import log
import json
import pickle

def entropy(dataset):#计算熵
    num = len(dataset)#样本数
    labelscount = {}
    for i in dataset:
        if i[-1] not in labelscount.keys():
            labelscount[i[-1]] = 1
        else:
            labelscount[i[-1]] += 1
    #labelscount 字典里面是样本类别的频数
    #print labelscount
    entropy_value = 0
    for key in labelscount:
        p = float(labelscount[key])/num
        entropy_value -= p*log(p, 2)
    return entropy_value

#dataset = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
#print entropy(dataset)

def dataset_split(dataset,feature_index,feature_value):#按照特征进行数据划分
    temp = []
    for feature_vector in dataset:
        if feature_vector[feature_index] == feature_value:
            ''' temp1 = []
            temp1.append(feature_vector[feature_index])
            temp1.append(feature_vector[-1])
            temp.append(temp1)'''
            reduce_feature_data=feature_vector[:feature_index]
            reduce_feature_data.extend(feature_vector[feature_index+1:])
            temp.append(reduce_feature_data)
    return temp
    


def choose_best_featue(dataset):#last colum of dataset is label,选取信息增益最大的特征
    feature_num = len(dataset[0])-1
    base_entropy = entropy(dataset)
    max_entropy = 0.0
    best_featue_index = -1# index
    for i in range(feature_num):
        feature_list = [temp[i] for temp in dataset]#第i个特征的list,一列
        feature_set = set(feature_list)
        feature_entropy = 0.0
        for value in feature_set:
            split_data = dataset_split(dataset,i,value)
            #print split_data
            feature_entropy += float(len(split_data))/len(dataset)*entropy(split_data)#

        if max_entropy < (base_entropy-feature_entropy):
            max_entropy = (base_entropy-feature_entropy)
            best_featue_index = i

    return best_featue_index



#=dataset_split(dataset,0,1)
#print r
#print dataset
#print choose_best_featue(dataset)


def majority_vote(group_list):#叶节点多数表决
    classcount={}
    for i in group_list:
        if i  not in classcount:
            classcount[i]=0
        classcount[i] += 1
    temp=classcount.items()
    sorted_classcount = sorted(temp,key=lambda classcount:classcount[1],reverse=True)
    return sorted_classcount[0][0]
    
def create_tree(dataset,feature_list):#dataset 
    label_list=[temp[-1] for temp in dataset]#dataset的label
    #停机条件
    if len(set(label_list))==1:#只有一类
        return label_list[0]
    if len(dataset[0]) == 1:#
        return majority_vote(label_list)
    #选取信息增益最大的特征
    best_featue_index=choose_best_featue(dataset)
    best_featue_tree=feature_list[best_featue_index]
    decision_tree={best_featue_tree:{}}#字典表示树
    del(feature_list[best_featue_index])#该特征已经被使用

    feature_set=set([temp[best_featue_index] for temp in dataset])
    #分叉
    for value in feature_set:
        temp_feature_list=feature_list[:]
        decision_tree[best_featue_tree][value] = create_tree(dataset_split(dataset,best_featue_index,value),temp_feature_list)
    #
    fw=open("decision_tree",'w')
    pickle.dump(decision_tree,fw)
    fw.close()
    return decision_tree



dataset = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no'],[1,0,'yes'],[1,0,'no']]
feature_list=['A','B']
tree = create_tree(dataset,feature_list)
tree_json=json.dumps(tree,indent=1)
print tree
#json.dumps(tree,indent=1)

#print choose_best_featue(dataset)

def classify(tree,test_vector,feature_list):
    root=tree.keys()[0]
    next_tree=tree[root]
    f_index=feature_list.index(root)#根节点的特征在输入的特在列表中的位置
    for key in next_tree.keys():
        if test_vector[f_index] == key:
            if type(next_tree[key]).__name__ == 'dict':
                class_label=classify(next_tree[key],test_vector,feature_list)
            else:
                class_label=next_tree[key]
    return class_label


test_vector=[1,1]
feature_list=['B','A']
fr=open('decision_tree')
store_tree=pickle.load(fr)
print '[1,1]',classify(store_tree,test_vector,feature_list)


'''a={'a':1,'b':2}
for i in a:
    print i 
'''




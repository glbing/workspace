#!/usr/bin/env python
# coding=utf-8

from numpy import *
import math
import matplotlib.pyplot as plt


def read_minutiae_xyt(filename):  # [x,y,direction,quality]
    fr = open(filename)
    minutiae_list = fr.readlines()
    minutiae_count = len(minutiae_list)
    # print minutiae_list
    minutiae_array = zeros([minutiae_count, 4])
    index = 0
    for line in minutiae_list:
        line = line.strip()  # 默认换行
        line = line.split()  # 默认空格
        minutiae_array[index] = line
        index += 1
    # print minutiae_array
    return minutiae_array, minutiae_count


def read_minutiae_min(filename):  # [[x,y],[direction,quality,type]]
    fr = open(filename)
    temp0 = fr.readlines()
    temp1 = []  # 文件每一行的数据都在里面
    temp2 = []  # 每一行的前2-5行
    minutiae_count = len(temp0) - 4  # 细节点个数
    minutiae_list = []
    coordinate_xy = [0, 0]
    coordinate_xy_array = zeros([minutiae_count, 2])
    angle = 0
    quality = 0.0
    type = ''
    # print len(minutiae_list)
    # print minutiae_list[5].strip()
    i = 0
    for line in temp0:
        line = line.strip()
        if i >= 4:
            line = line.split(':')
            for i in range(len(line)):
                line[i] = line[i].strip()
            temp1.append(line)
            temp2.append(line[1:5])
            # print len(line)
        i += 1
    # print temp1[5]
    # print temp2[6]
    index = 0
    for i in temp2:
        # print i
        minutiae = []
        t_xy = i[0].split(',')
        t_xy[0] = int(t_xy[0].strip())
        t_xy[1] = int(t_xy[1].strip())
        coordinate_xy = t_xy
        angle = int(i[1])
        quality = float(i[2])
        type = i[3]

        minutiae.append(coordinate_xy)
        minutiae.append(angle)
        minutiae.append(quality)
        minutiae.append(type)
        minutiae_list.append(minutiae)
        coordinate_xy_array[index] = coordinate_xy
        index += 1
        # print minutiae

    # print minutiae_count
    # print coordinate_xy_array
    return minutiae_list, minutiae_count, coordinate_xy_array


def plt_minutiae(minutiae_array):
    temp = minutiae_array
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title("minutiae distribution")
    # ax.scatter(temp[:,0],temp[:,1],temp[:,3])#大小表示质量好坏
    ax.scatter(temp[:, 0], temp[:, 1])
    plt.show()


def get_neighbors(coordinate_xy_array, n):  # 输入是xy坐标数组和最近邻的个数
    neighbor_list = []
    for i in range(len(coordinate_xy_array)):
        distance_list = []
        for j in range(len(coordinate_xy_array)):
            d = (coordinate_xy_array[i][0] - coordinate_xy_array[j][0])**2 + \
                (coordinate_xy_array[i][1] - coordinate_xy_array[j][1])**2
            # if j != i:
            distance_list.append(d)
        # print len(distance_list)
        sorted_indices = array(distance_list).argsort()
        neighbor_list.append(list(sorted_indices[:n + 1]))
    # print neighbor_list
    neighbor_array = array(neighbor_list)
    # print neighbor_array
    # print t
    return neighbor_array[:, 1:]


def triangle(minutiae_list, neighbor_indices):  # 输入为细节点列表和对应的n个最近邻
    # n = len(neighbor_indices[0])#邻点个数
    # print n

    # relative_distance
    # relative_orientation
    # triangle_angle
    minutiae_feature_set=[]#细节点特征向量集合

    for i in range(len(minutiae_list)):  # 对每个细节点构造n*3维的特征向量
        minutiae_feature=[]#i的特作向量
        for j in range(len(neighbor_indices[0])):

            d_A = ((minutiae_list[i][0][0] - minutiae_list[neighbor_indices[i][j]][0][0])**2 +
                   (minutiae_list[i][0][1] - minutiae_list[neighbor_indices[i][j]][0][1])**2)**0.5

            d_B = ((minutiae_list[i][0][0] - minutiae_list[neighbor_indices[i][(j + 1) % (len(neighbor_indices[0]))]][0][0])**2 +
                   (minutiae_list[i][0][1] - minutiae_list[neighbor_indices[i][(j + 1) % (len(neighbor_indices[0]))]][0][1])**2)**0.5 

            d_AB=((minutiae_list[neighbor_indices[i][j]][0][0]- minutiae_list[neighbor_indices[i][(j + 1) % (len(neighbor_indices[0]))]][0][0])**2+ (minutiae_list[neighbor_indices[i][j]][0][1]- minutiae_list[neighbor_indices[i][(j + 1) % (len(neighbor_indices[0]))]][0][1])**2)**0.5
            #print d_A
            #print d_B_
            #print d_AB
            # print type(d_A)
            # 除数为 0 ？？？？？？？？
            relative_distance = d_A / d_B
            #print relative_distance

            o_A = float(minutiae_list[neighbor_indices[i][j]][1] - minutiae_list[i][1])
            o_B = float(minutiae_list[neighbor_indices[i][(j + 1) % \
                    (len( neighbor_indices[0]))]][1] - minutiae_list[i][1])
            if o_B == 0:#当除数是0时，可以规定一个值，如 -1  ？？
                relative_orientation = -1 
            else:
                relative_orientation= o_A/o_B
            # print relative_orientation
            
            cos_A=(d_A**2+d_AB**2-d_B**2)/(2*d_A*d_AB)
            cos_B=(d_B**2+d_AB**2-d_A**2)/(2*d_B*d_AB)
            #print cos_A
            #print cos_B
            t_A=math.degrees(math.acos(cos_A))
            t_B=math.degrees(math.acos(cos_B))
            relative_angle=t_A/t_B
            #print t_A
            #print t_B
            #print t_A/t_B
            minutiae_feature.append([relative_distance,relative_orientation,relative_angle])
        minutiae_feature_set.append(array(minutiae_feature))
    return minutiae_feature_set

if __name__ == '__main__':

    minutiae_array, minutiae_count = read_minutiae_xyt(
        '../temp/101_4/101_4.xyt')
    # plt_minutiae(minutiae_arra

    minutiae_list, minutiae_count, coordinate_xy_array = read_minutiae_min(
        '../temp/101_4/101_4.min')
    # plt_minutiae(coordinate_xy_array)
    # print minutiae_list
    # print coordinate_xy_array

    neighbor_indices = get_neighbors(coordinate_xy_array, 5)
    # print neighbor_indices
    '''
    for i in neighbor_indices:
        print coordinate_xy_array[i][0]
    '''
    minutiae_feature_set=triangle(minutiae_list, neighbor_indices)#返回一个指纹的特征向量集合，集合大小为
    #细节点的数量，集合元素为5*3的特作向量数组
    print minutiae_feature_set[18]
    print type(minutiae_feature_set)

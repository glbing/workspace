#!/usr/bin/env python
# coding=utf-8
from minutiae_feature import *
from numpy import *


def distance(a, b):  # 距离函数
    return sqrt(sum((a - b)**2))


def centriods_init(dataset, k):  # dataset是数据集合，k是质心的个数
    t0 = [k]
    t1 = list(shape(dataset[0]))
    t0.extend(t1)
    dimension = t0
    # print dimension
    centriods = zeros(dimension)
    for i in range(len(dataset[0])):
        for j in range(len(dataset[0][0])):
            min_ = min(dataset[:, i, j])
            max_ = max(dataset[:, i, j])
            range_ = max_ - min_
            centriods[:, i, j] = min_ + range_ * (random.rand(k, 1)[:, 0])
    return centriods

# 利用聚类，无监督的学习出 最终的 centriods 和 cluster_label


def k_means(dataset, k, funiction_distance=distance,
            function_centriod=centriods_init):
    dataset_count = len(dataset)
    cluster_label = zeros([dataset_count, 2])  # 聚类标注向量，记录簇索引和离簇的距离
    # cluster_label -= 1  # 初始化为 -1，
    # print cluster_label
    centriods = centriods_init(dataset, k)  # 初始化质心
    # print centriods
    cluetr_flag = True  # 聚类结束标志
    while cluetr_flag:
        cluetr_flag = False
        for i in range(dataset_count):
            min_dist = inf  # 无穷大
            min_index = -1  # 初始簇索引为-1
            for j in range(k):
                # centriods,kx5x3
                d = funiction_distance(dataset[i], centriods[j])
                # print d
                if d < min_dist:
                    min_dist = d
                    min_index = j
                    # print min_dist
            # print min_dist
            if cluster_label[i, 0] != min_index:
                cluetr_flag = True
                cluster_label[i, 0] = min_index
                cluster_label[i, 1] = min_dist

            # print 'jjjjjj'

        # print centriods
        # 对每个点进行了一轮簇的分配后，再跟新质心向量
        for l in range(k):
            sum = zeros([5, 3])
            count = 0
            for z in range(dataset_count):
                if l == cluster_label[z, 0]:
                    sum += dataset[z]
                    count += 1
            if count != 0:
                centriods[l] = sum / count

        # print '聚类'
    return centriods, cluster_label

if __name__ == '__main__':
    minutiae_list, minutiae_count, coordinate_xy_array = read_minutiae_min(
        '../temp/101_4/101_4.min')
    neighbor_indeces = get_neighbors(coordinate_xy_array, 5)
    minutiae_feature_set = triangle(minutiae_list, neighbor_indeces)
    minutiae_feature_set = array(minutiae_feature_set)  # list转换为数组
    # print type(minutiae_feature_set)
    # print minutiae_feature_set[1]
    # print '\n'
    # print minutiae_feature_set[8]
    # print '\n'
    # d = distance(minutiae_feature_set[1], minutiae_feature_set[8])
    #centriods = centriods_init(minutiae_feature_set, 100)
    # print centriods
    centriods, cluster_label = k_means(minutiae_feature_set, 1000)
    print centriods
    print cluster_label

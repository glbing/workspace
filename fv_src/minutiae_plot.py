#!/usr/bin/env python
# coding=utf-8

from numpy import *
import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def read_minutiae_xyt(filename):
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
    fr.close()
    return minutiae_array, minutiae_count


# DIR= ../temp/s0024301/
# create .raw,jpb : ./command.txt

def read_fingerprint(filename):
    img = Image.open(filename)
    img_array = array(img)  # 转换为二维数组
    img_height = len(img_array)
    img_width = len(img_array[0])
    # img.show()
    return img, img_array, img_height, img_width


def minutiae_plot_1(minutiae_array):  # 散点图
    temp = minutiae_array
    plt.title("minutiae distribution")
    # ax.scatter(temp[:,0],temp[:,1],temp[:,3])#大小表示质量好坏
    plt.scatter(temp[:, 0], temp[:, 1])
    plt.show()


def minutiae_plot_2(minutiae_file, fingerprint_file):  # 叠加
    minutiae_array, minutiae_count = read_minutiae_xyt(minutiae_file)
    img, img_array, img_height, img_width = read_fingerprint(fingerprint_file)

    #print (img_height,img_width)
    plt.imshow(img_array, cmap=cm.gray)  # 这里注意，要指定灰度图
    plt.plot(minutiae_array[:, 0], minutiae_array[:, 1], 'r*')

    plt.title("minutiae distribution")
    # plt.xlabel('width')
    # plt.ylabel('height')
    plt.show()
    plt.axis('off')


if __name__ == '__main__':

    # minutiae_plot_1(minutiae_array)
    minutiae_plot_2('../temp/107_2/107_2.xyt', '../temp/107_2/107_2.jpg')

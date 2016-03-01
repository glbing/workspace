#!/usr/bin/env python
# coding=utf-8
import os
import pickle#序列化 /反序列化
from numpy import *
from minutiae_feature import *
from clustering import *

FVC_DB1='/home/glb/fingerprint_verification_1.1/fvc_minutiae_db/DB1_B'
FVC_DB2='/home/glb/fingerprint_verification_1.1/fvc_minutiae_db/DB2_B'
FVC_DB3='/home/glb/fingerprint_verification_1.1/fvc_minutiae_db/DB3_B/'
FVC_DB4='/home/glb/fingerprint_verification_1.1/fvc_minutiae_db/DB4_B/'

if __name__ == '__main__':
    minutiae_list, minutiae_count, coordinate_xy_array = read_minutiae_min(
        '../temp/101_2/101_2.min')
    neighbor_indeces = get_neighbors(coordinate_xy_array, 5)
    minutiae_feature_set = array(triangle(minutiae_list, neighbor_indeces))
    # print minutiae_feature_set[10]

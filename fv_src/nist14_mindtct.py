#!/usr/bin/env python
# coding=utf-8

import os

MINDTCT='/home/glb/NBIS/Main/bin/mindtct'
DATA='../nist14_db/'
OUTPUT='../nist14_minutiae_db/'

def mindtct():
    if os.path.exists(MINDTCT) == False:
        print "ERROR: %s is not a path to the mindtct program" %MINDTCT
        return
    elif os.path.exists(DATA) == False:
        print "ERROR: %s is not a path to a  directory" %DATA
        return
    elif os.path.exists(OUTPUT) == False:
        print "ERROR: %s is not a path to a  directory" %OUTPUT
        return
    else:
        print ""
        print "minutiae dectecting,please wait\n"
        print "....................."
        print "....................."

    img_list=os.listdir(DATA)
    img_list.sort()#按照文件名排序
    img_list_len=len(img_list)
    minutiae_list=[]
    for i in range(img_list_len):
        minutiae_list.append(img_list[i].split('.')[0])

    #print len(minutiae_list)
    #print minutiae_list
    for i in range(img_list_len):
        os.mkdir(OUTPUT+minutiae_list[i])
        cmd=MINDTCT+' ' + '-b'+' '+'-m1'+' '+DATA+img_list[i]+' '+OUTPUT+minutiae_list[i]+'/'+minutiae_list[i]
        print cmd
        os.system(cmd)
        
    return

if __name__ == '__main__':
    mindtct()



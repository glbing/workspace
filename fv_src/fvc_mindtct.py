#!/usr/bin/env python
# coding=utf-8

import os

MINDTCT='/home/glb/NBIS/Main/bin/mindtct'
DATA='../fvc_db/'
OUTPUT='../fvc_minutiae_db/'

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

    dir_list=os.listdir(DATA)
    dir_list.sort()
    out_dir_list=[]
    for i in range(len(dir_list)):
        out_dir_list.append(dir_list[i]+'/')
    print dir_list

    for i in range(len(dir_list)):
        dir_list[i]=DATA+dir_list[i]+'/'
    print dir_list

    for i in range(len(dir_list)):

        img_list=os.listdir(dir_list[i])
        img_list.sort()
        #print img_list.sort

        img_list_len=len(img_list)
        minutiae_list=[]
        for j in range(img_list_len):
            minutiae_list.append(img_list[j].split('.')[0])

        #print len(minutiae_list)
        #print minutiae_list
        for k in range(img_list_len):
            os.mkdir(OUTPUT+out_dir_list[i]+minutiae_list[k])
            #print OUTPUT+out_dir_list[i]+minutiae_list[k]
            cmd=MINDTCT+' ' + '-b'+' '+'-m1'+' '+dir_list[i]+img_list[k]+' '+OUTPUT+out_dir_list[i]+minutiae_list[k]+'/'+minutiae_list[k]
            print cmd
            os.system(cmd)

    return

if __name__ == '__main__':
    mindtct()



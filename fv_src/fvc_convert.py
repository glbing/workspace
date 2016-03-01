#!/usr/bin/env python
# coding=utf-8

import os
import Image
MINDTCT='/home/glb/NBIS/Main/bin/mindtct'
DATA='../fvc_db/'
#OUTPUT='../fvc_minutiae_db/'

def mindtct():
    if os.path.exists(MINDTCT) == False:
        print "ERROR: %s is not a path to the mindtct program" %MINDTCT
        return
    elif os.path.exists(DATA) == False:
        print "ERROR: %s is not a path to a  directory" %DATA
        return
    else:
        print ""
        print "minutiae dectecting,please wait\n"
        print "....................."
        print "....................."

    dir_list=os.listdir(DATA)
    #print dir_list

    for i in range(len(dir_list)):
        dir_list[i]=DATA+dir_list[i]+'/'
    #print dir_list

    for i in range(len(dir_list)):

        img_list=os.listdir(dir_list[i])
        img_list.sort()
        #print img_list.sort

        img_list_len=len(img_list)
        input=[]
        output=[]#输出
        for j in range(img_list_len):
            input.append(dir_list[i]+img_list[j])
            output.append(dir_list[i]+img_list[j].split('.')[0]+'.jpg')
            #img_list[j]=dir_list[i]+img_list[j]
        #print input 
        
        for k in range(img_list_len):
            img=Image.open(input[k])
            img.save(output[k],'JPEG')
            os.system('rm '+input[k])

    return

if __name__ == '__main__':
    mindtct()



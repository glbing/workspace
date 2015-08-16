#!/usr/bin/env python
# coding=utf-8
import os
import time

#source=['/home/code/','/home/python/']
source=[]
source.append(input('input the dir that you need to bakup:\n'))
print(source)
target_dir='/home/backup/'
target_dir=target_dir+time.strftime('%Y%m%d')+'/'
if os.path.exists(target_dir)==False:
    os.mkdir(target_dir)
    print('mkdir successfully')    
target=target_dir+time.strftime('%H%M%S')+'.zip '
zip_commmand="zip -qr "+target+' '.join(source)
print(zip_commmand)
#run
if os.system(zip_commmand)==0:
    print("backup successfully")
else:
    print("backup \
          failed")
#os.system("ls")


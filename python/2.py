#!/usr/bin/env python
# coding=utf-8
def functioin1():
    print("hello world\n")
#function1()
def function2(a,b=8,c=9):
    print(a+b+c)
    return (a+c)
function2(2,3)
function2(4,b=9)
k=function2(2,c=6)
print(k)
#i=9
global i
i=99
for j in range(1,4):
    i=i+1;
print(i)

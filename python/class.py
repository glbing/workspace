#!/usr/bin/env python
# coding=utf-8
class person:
#    num=0;
    def hello(self,a=3):
        a=str(a)
        print("hello world "+a)
    def __init__(self,name):
        self.name=name
        person.num=1
    def __del__(self):
        pass
    num=0
p=person("glb")
print(person.num)
p.hello(23)
p.hello()


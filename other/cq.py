#coding:utf-8
import random as r
#
# name = []
# a = r.sample(name,3)
# z = a[0]
# x = a[1]
# c = a[2]
# print z,x,c
#九九乘法表
for i in range(0,10):
    for j in range(1,i+1):
        print str(i)+"*"+str(j)+"="+str(i*j),
    print " "



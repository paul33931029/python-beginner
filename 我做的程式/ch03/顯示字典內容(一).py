# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 20:21:23 2018

@author: Paul
"""

dict1={"林小明":85,"黃明晶":71,"曾山水":93,}
dict1.setdefault("陳莉莉",98)
dict1.setdefault("鄭美麗",67)
name=list(dict1.keys())
score=list(dict1.values())
for i in range(0,5):
    print("%s 的成績為:%s分"%(name[i],score[i]))
    i+=1

#林小明   黃明晶    曾山水    陳莉莉    鄭美麗
#85   71    93    98 67
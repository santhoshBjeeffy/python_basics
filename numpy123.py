# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 08:37:58 2018

@author: santhob
"""

# minimum dimensions 
import numpy as np1
import time
import sys

'''a=np1. array([1,2,5,3,7])
print(a)

s=range(10000000)
print(sys.getsizeof(8)*len(s))  

b=np1.arange(10000000)
print(b.size*b.itemsize)
'''
size=10000000
l1=range(size)
l2=range(size)

A1=np1.arange(size)
A2=np1.arange(size)

start=time.time()

result=[(x,y) for x,y in zip(l1,l2)]

print((time.time()-start)*1000)

start=time.time()

result=A1+A2

print((time.time()-start)*1000)
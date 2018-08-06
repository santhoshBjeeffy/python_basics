# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 09:29:16 2018

@author: santhob
"""

X=10
print (X)
y=2+3
print(y)
print(X+y)
X=2
print(X)
name ="youtube"    
print(name)
print(name[1:3])
print(name[1:])
print(name[:3])
print(name[1:13])
print(name[-2])
'''name[2]="A" string is immutable in python also once it is assigned cant be changed
'''
print("my" + name[3:7])
myname="santhosh"
print(len(myname))

''' list starts '''


runs=[24,45,2,3,5,7,1]
print(runs)
print(runs[2])
print(runs[2:])
print(runs[1:15])
print(runs[-1])

names=["runs", "sbc", "xyz"]
print(names)
print(names[2])
'''variables with different types also possible'''

misc=["abc",123,"santh0sh"]
print(misc)
print(misc[2])

mil=[names,misc]
print(mil)
runs.append(60)
print(runs)
runs.insert(2,100)
print(runs)
runs.remove(5)
print(runs)
print(runs.pop(1))
print(runs)
print(runs.pop())
print(runs)
del runs[2:]
print(runs)
runs.extend([12,34,6,67])
print(runs)
print(sum(runs))
runs.sort()
print(runs)

'''list is mutable we can change anytime'''
tup=(12,14,25)
print(tup)
'''tup[1]=34  tuple is same as list but its immutable we cant change the value and perofrmance is fast then list will be defined with round brackets'''
print(tup[1])

s={1,2,4,3,6,1,23,23}
print(s)
num=5
print(id(num))
name='santhosh'
print(id(name))
a=10
b=a

print(id(a))
print(id(b))
print(type(a))

'''print(s[2]) will not support indexing set will not maintain duplicate values and set will be not in sorted order it will use hashing mechanish
performance will be faster if we dont care about the orde as it will go and fetch ASAP

s.sort()
print(s)
'''
import numpy


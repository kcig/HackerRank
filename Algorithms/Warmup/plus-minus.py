#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
pos = 0
neg = 0
zer = 0

for el in arr:
    if el > 0:
        pos+=1
    elif el == 0:
        zer+=1
    elif el < 0:
        neg+=1
        
print float(pos)/float(n)
print float(neg)/float(n)
print float(zer)/float(n)
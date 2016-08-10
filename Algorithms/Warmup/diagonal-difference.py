#!/bin/python

import sys

n = int(raw_input().strip())
a = []
primaryDiagonal = 0
secondaryDiagonal = 0
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
    primaryDiagonal += a_temp[a_i]
    secondaryDiagonal += a_temp[n-a_i-1]
    
print abs(primaryDiagonal - secondaryDiagonal)

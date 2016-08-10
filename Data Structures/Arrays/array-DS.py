#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
output = ''
while n-1 >= 0 :
    output = output + str(arr[n-1])
    if n-1 !=0:
        output = output + ' '
    n-=1
print output
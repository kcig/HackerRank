#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
s=6
hourglassSums = []
for x in range(s-3, s+1): # columns
    for y in range(s-3, s+1): # rows
        hourglassSums.append(arr[x-3][y-3] + arr[x-3][y-2] + arr[x-3][y-1] + arr[x-2][y-2] + arr[x-1][y-3] + arr[x-1][y-2] + arr[x-1][y-1])

print max( hourglassSums )

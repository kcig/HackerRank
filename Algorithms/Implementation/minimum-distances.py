#!/bin/python

import sys


n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))
B = {}
for index,item in enumerate(A):
    if A.count(item) > 1:
        if item in B.keys():
            #add index to dict list
            B[item].append(index)
        else:
            #add key that has index
            B[item] = [index]


smallest_index = -1

for key, indexes in B.iteritems():
    for x in range( len(indexes)-1 ):
        distance = indexes[x+1] - indexes[x]
        if smallest_index > 0 and distance < smallest_index:
            smallest_index = distance
        elif smallest_index < 0:
            smallest_index = distance

print smallest_index
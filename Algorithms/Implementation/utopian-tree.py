#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip()) #growth cycles
    h = 1
    for x in range(n):
        if x%2 == 0:
            h = h*2
        else:
            h = h+1
    print h
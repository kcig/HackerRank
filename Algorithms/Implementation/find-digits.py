#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    digits = [int(x) for x in str(n)]
    count=0
    for d in digits:
        if d !=0 and n%d ==0:
            count+=1
    print count
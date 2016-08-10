#!/bin/python

import sys


n = int(raw_input().strip())

for s in range(n):
    #s=0 - first stair, needs to have 5 spaces and 1 #
    spaces = n-1-s
    hashes = n-spaces
    print spaces*' '+'#'*hashes

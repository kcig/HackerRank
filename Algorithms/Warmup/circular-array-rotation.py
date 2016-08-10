#!/bin/python

n,k,q = map( int, raw_input().split(' ') )
array = raw_input().split(' ')
    
r = k%n
    
for x in range(q):
    rotated_index = int(raw_input())
    
    index = ( rotated_index - r ) % (n)
    print array[ index ]
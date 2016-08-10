#!/bin/python
def insertionSort(ar):
    for x in range(0,len(ar)-1):
        if ar[x+1] >= ar[x]:
            #don't move it
            print ' '.join( [ str(el) for el in ar] )
        elif ar[x+1] < ar[x]:
            #move value over
            y = x
            while y >= 0 and ar[y+1] < ar[y]:
                ar[y] , ar[y+1] = ar[y+1], ar[y]
                y-=1
            print ' '.join( [ str(el) for el in ar] )
    return ""


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
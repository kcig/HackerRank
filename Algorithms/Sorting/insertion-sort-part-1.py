#!/bin/python
def insertionSort(ar):
    e = ar[-1]
    x=1
    sorted = False
    for el in reversed(ar[0:-1]):
        if el > e:
            ar[ m-x ] = el
            print ' '.join(map(str,ar))
            x+=1
        elif el < e:
            ar[m-x] = e
            print ' '.join(map(str,ar))
            sorted = True
            break
    if sorted == False:
        ar[0] = e
        print ' '.join(map(str,ar))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
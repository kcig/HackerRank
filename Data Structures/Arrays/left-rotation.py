q= map(int,raw_input().strip().split(' '))
N = q[0]
d = q[1]
arr = map(int,raw_input().strip().split(' '))
i=0

while i < d:
    shift = arr[0]
    arr.pop(0)
    arr.append(shift)
    i+=1

print (' ').join( map(str, arr) )
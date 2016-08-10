N = int(raw_input().strip())
strings = []

for x in range(N):
    strings.append(raw_input().strip())
    
Q = int(raw_input().strip())
queries = []

for x in range(Q):
    queries.append( raw_input().strip() )

for q in queries:
    print strings.count(q)
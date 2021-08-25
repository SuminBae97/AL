import heapq
import sys
n = int(sys.stdin.readline())
max_heap =[]
for i in range(n):
    val = int(sys.stdin.readline())
    if val ==0:
        if len(max_heap)!=0:
            a = (heapq.heappop(max_heap))
            print(a[1])
        else:
            print(0)

    else:
        heapq.heappush(max_heap,(-val,val))












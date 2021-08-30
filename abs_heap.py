import heapq
import sys
heap =[]

n = int(sys.stdin.readline())

for _ in range(n):
    val = int(sys.stdin.readline())

    if val != 0:
        heapq.heappush(heap, (abs(val), val))

    elif val == 0:
        if len(heap) == 0:
            print(0)
        else:
            abs_val, val1 = heapq.heappop(heap)
            print(val1)












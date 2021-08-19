import itertools
import sys

n,m=map(int,sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))

ncr = itertools.combinations(cards,3)
result = 0
for a,b,c in ncr:
    sumf = a+b+c
    if sumf > m:
        continue
    else:
        result = max(result,sumf)

print(result)


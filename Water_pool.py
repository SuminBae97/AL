import sys
n,m = map(int,sys.stdin.readline().split())
pillar = list(map(int,sys.stdin.readline().split()))
raindrop=0
for i in range(m):
    left_max = max(pillar[:i+1])
    right_max = max(pillar[i:])

    lowe  = min(left_max,right_max)
    raindrop = raindrop + abs(pillar[i] - lowe)


print(raindrop)

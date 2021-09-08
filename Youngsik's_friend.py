import sys
from collections import deque

n,m,l = map(int,sys.stdin.readline().split())
friends = [0 for _ in range(n)]
friends=deque(friends)

friends[0]=1
count=0
while m not in friends:
    if friends[0]%2==0:
        friends.rotate(-l)
        friends[0]+=1
        count+=1

    else:
        friends.rotate(l)
        friends[0]+=1
        count+=1

print(count)

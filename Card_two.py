import sys
from collections import deque
n = int(sys.stdin.readline())
q=deque()

for val in range(1,n+1):
    q.append(val)


while len(q)!=1:
    q.popleft()
    second = q.popleft()
    q.append(second)

print(q.popleft())
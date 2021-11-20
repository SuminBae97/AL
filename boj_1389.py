import sys
from collections import deque


# 5 5
# 1 3
# 1 4
# 4 5
# 4 3
# 3 2

n,m = map(int,sys.stdin.readline().split())
graph = [[] for _  in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    dist = [0] * (n + 1)
    visited = [0] * (n + 1)
    q = deque([start])
    visited[start]=True
    while q:
        val = q.popleft()
        for nxt in graph[val]:
            if visited[nxt]==False:
                visited[nxt]=True
                q.append(nxt)
                dist[nxt] = dist[val]+1
    return sum(dist)
result=[]
for i in range(1,n+1):
    result.append(bfs(i))

print(result.index(min(result))+1)
# result = [INF]
# for i in range(1,n+1):
#     distance = [0 for _ in range(n+1)]
#     visited = [False for _ in range(n+1)]
#     bfs(i)
#     result.append(sum(distance))
#

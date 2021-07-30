import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
visited = [False]*(n+1)
graph=[[] for _  in range(n+1)]

for _ in range(m):
    i,j = map(int,sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)



def bfs(i):
    q=deque()
    q.append(i)
    visited[i] = True

    while q:
        val =q.popleft()
        for j in graph[val]:
            if not visited[j]:
                q.append(j)
                visited[j]=True

count=0

for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        count+=1
print(count)



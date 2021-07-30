
import sys
sys.setrecursionlimit(100000)
N,M=map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph,i,visited):
    visited[i]=True
    for val in graph[i]:
        if not visited[val]:
            dfs(graph,val,visited)

count =0

for i in range(1,N+1):
    if not visited[i]:
        dfs(graph,i,visited)
        count+=1

print(count)












import sys
from collections import deque
from pprint import pprint

dx = [1,-1,0,0]
dy = [0,0,1,-1]


n,m = map(int,sys.stdin.readline().split())

graph =[]
for _ in range(n):
    tmp =list(map(int,sys.stdin.readline().split(" ")))
    graph.append(tmp)

visited = [[False]*m for _ in range(n)]
result=[]

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y]=True
    oct=0
    while q:
        x_,y_ = q.popleft()
        for i in range(4):
            nx = x_+dx[i]
            ny = y_+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            elif visited[nx][ny]==False and graph[nx][ny]==0:
                q.append([nx,ny])
                visited[nx][ny]=True

            elif visited[nx][ny]==False and graph[nx][ny]==1:
                visited[nx][ny]=True
                graph[nx][ny]=0
                oct +=1
    return oct


count=0
while sum(sum(graph,[]))!=0:
    oct = bfs(0,0)
    result.append(oct)
    visited = [[False] * m for _ in range(n)]
    count+=1



print(count)
print(oct)










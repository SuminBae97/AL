import sys
from collections import deque

m,n = map(int,sys.stdin.readline().split())
graph=[]
for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    graph.append(tmp)
dx=[1,-1,0,0]
dy=[0,0,1,-1]

visited = [[False]*m for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            q.append([i,j])


def bfs(x,y):
    while q:
        _x,_y = q.popleft()
        for i in range(4):
            nx = _x+dx[i]
            ny = _y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            elif graph[nx][ny]==0:
                q.append([nx,ny])
                graph[nx][ny]=graph[_x][_y]+1
                visited[nx][ny]=True



for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            bfs(i,j)



answ = 0
for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    answ = max(answ,max(i))
print(answ-1)
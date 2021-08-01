import sys
from collections import deque
n= int(input())
graph=[]

dx=[1,-1,0,0]
dy=[0,0,1,-1]


for _ in range(n):
    tmp = list(sys.stdin.readline().rstrip())
    graph.append(tmp)

visited = [[False] * n for _ in range(n)]

def bfs(x,y,color):
    q=deque()
    q.append([x,y])
    visited[x][y]=True

    while q:
        _x,_y=q.popleft()
        for i in range(4):
            nx = _x+dx[i]
            ny = _y + dy[i]

            if nx>=n or nx<0 or ny<0 or ny>=n:
                continue

            elif graph[nx][ny]==color and visited[nx][ny]!=True:
                q.append([nx,ny])
                visited[nx][ny]=True



cnt=0
for color in ["R","G","B"]:
    for i in range(n):
        for j in range(n):
            if graph[i][j] == color and visited[i][j] != True:
                bfs(i, j,color)
                cnt += 1
print(cnt,end=" ")

cn2=0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
visited = [[False] * n for _ in range(n)]

for color in ["G","B"]:
    for i in range(n):
        for j in range(n):
            if graph[i][j] == color and visited[i][j] != True:
                bfs(i, j,color)
                cn2 += 1
print(cn2)
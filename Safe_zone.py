import sys
from collections import deque
n = int(input())
graph = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))


def bfs(x,y,h):
    q=deque()
    q.append([x,y])
    visited[x][y]=True
    while q:
        _x,_y = q.popleft()
        for i in range(4):
            nx = _x+dx[i]
            ny = _y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            elif graph[nx][ny]>h and visited[nx][ny]!=True:
                visited[nx][ny]=True
                q.append([nx,ny])
result=[]
for height in range(0,101):
    count = 0
    #visited 를 매번 높이별로 초기화하는거 생깍해라 멍청아
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]!=True and graph[i][j]>height:
                bfs(i,j,height)
                count+=1
    result.append(count)

print(max(result))




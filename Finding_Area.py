from collections import deque
import sys
M,N,r = map(int,sys.stdin.readline().split())
graph =[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for _ in range(M):
    graph.append([1]*N)


visited = [[False]*N for _ in range(M)]

for _ in range(r):
    x1,y1,x2,y2= map(int,sys.stdin.readline().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[j][i]=0


def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=True
    count=1

    while q:
        _x,_y=q.popleft()

        for i in range(4):
            nx = _x+dx[i]
            ny = _y+dy[i]

            if nx<0 or nx>=M or ny<0 or  ny>=N:
                continue

            elif graph[nx][ny]==1 and visited[nx][ny]==False:
                q.append([nx,ny])
                visited[nx][ny]=True
                count+=1
    return count

cnt = 0
ans=[]
for i in range(M):
    for j in range(N):
        if graph[i][j]!=0 and visited[i][j]==False:
            c =bfs(i,j)
            cnt+=1
            if c!=0:
                ans.append(c)

print(cnt)
ans.sort()
for val in ans:
    print(val,end=" ")

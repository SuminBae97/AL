import sys
from collections import deque

coord = [
    [1,0],
    [-1,0],
    [0,1],
    [0,-1],
    [1,1],
    [1,-1],
    [-1,1],
    [-1,-1]
]


def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y]=0

    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x + coord[i][0]
            ny = y + coord[i][1]

            if nx <0 or nx>=n or ny>=m or ny<0:
                continue

            elif graph[nx][ny]==1:
                q.append((nx, ny))
                graph[nx][ny]=0


while 1:
    #m,n =map(int,input().split())
    m,n = map(int, sys.stdin.readline().split())

    if m == 0 and n == 0:
        break

    graph = []
    for _ in range(n):
        #tmp =list(map(int,input().split()))
        tmp = list(map(int, sys.stdin.readline().split()))
        graph.append(tmp)

    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                bfs(i, j)
                count += 1
    print(count)






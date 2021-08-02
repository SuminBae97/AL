import sys
from collections import deque
test_case = int(input())

coord=[
    [1,2],
    [2,1],
    [2,-1],
    [1,-2],
    [-1,2],
    [-2,1],
    [-1,-2],
    [-2,-1]
]
def bfs(x,y,x_p,y_p):
    q = deque()
    q.append([x,y])
    visited[x][y]=True

    while q:
        x_,y_ = q.popleft()
        for i in range(8):
            nx = x_+coord[i][0]
            ny = y_+coord[i][1]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            elif nx==x_p and ny==y_p:
                graph[nx][ny] = graph[x_][y_]+1
                return

            elif visited[nx][ny]!=True:
                graph[nx][ny] = graph[x_][y_] + 1
                visited[nx][ny]=True
                q.append([nx,ny])


for _ in range(test_case):
    n = int(input())

    graph = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    a, b = map(int, input().split())
    c, d = map(int, input().split())

    if a==c and b==d:
        print(0)

    else:
        bfs(a,b,c,d)
        print(graph[c][d])





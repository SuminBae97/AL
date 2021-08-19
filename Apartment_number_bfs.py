import sys
sys.setrecursionlimit(10**6)
from functools import reduce
from collections import deque,Counter

n= int(sys.stdin.readline())
graph = []
visited  = [[False]*n for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))


dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt=0

def bfs(x,y,cnt):
    q = deque()
    visited[x][y]=True
    graph[x][y]=cnt
    q.append([x,y])
    while q:
        xp,yp = q.popleft()

        for i in range(4):
            nx = xp+dx[i]
            ny = yp+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            elif graph[nx][ny]==1 and visited[nx][ny]!=True:
                q.append([nx,ny])
                visited[nx][ny]=True
                graph[nx][ny]=cnt




for i in range(n):
    for j in range(n):
        if visited[i][j]!=True and graph[i][j]==1:
            cnt+=1
            bfs(i,j,cnt)






print(cnt)
# 각 단지마다 집 개수 출력
# 2차원 배열을 1차원으로 쭈욱 펼치기
ans = reduce(lambda x,y : x+y, graph)
# 단지로 등록?된 집들만 ans 리스트에 남기기
ans = [x for x in ans if x > 0]
# cnt(단지번호) 별 개수(Counter.values()) 구하고 출력
ans = sorted(list(Counter(ans).values()))
print('\n'.join(map(str,ans)))

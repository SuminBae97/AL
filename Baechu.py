import sys
sys.setrecursionlimit(10**6)
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

test_case = int(input())
result=[]
for i in range(test_case):
    n, m, b = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append([0] * m)

    for _ in range(b):
        x, y = map(int, input().split())
        graph[x][y] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j)==True:
                count+=1



    print(count)




# n,m,b = map(int,input().split())
# graph =[]
# for _ in range(n):
#     graph.append([0]*m)
#
# for _ in range(b):
#     x,y = map(int,input().split())
#     graph[x][y]=1
#
#
#
#
# count=0
# for i in range(n):
#     for j in range(m):
#         if dfs(i,j)==True:
#             count+=1
#
# print(count)
#

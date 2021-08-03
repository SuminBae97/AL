import sys
sys.setrecursionlimit(10**6)
n= int(input())
tree=[[] for _ in range(n+1)]

parent=[0 for i in range(n+1)]

for i in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(start,tree,parent):
    for i in tree[start]:
        if parent[i]==0:
            parent[i]=start

            dfs(i,tree,parent)


dfs(1,tree,parent)

for i in range(2,n+1):
    print(parent[i])


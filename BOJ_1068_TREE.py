import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
tree = list(map(int,sys.stdin.readline().split()))
del_node = int(sys.stdin.readline())


def dfs(start,tree):
    tree[start] = -2

    for i in range(len(tree)):
        if tree[start]==i:
            dfs(i,tree)
            






# def dfs(start,tree):
#     tree[start]=-2
#
#     for i in range(len(tree)):
#         if tree[i]==start:
#             dfs(i,tree)
#
#
# dfs(del_node,tree)
#
# count=0
# for i in range(len(tree)):
#     if tree[i]!=-2 and i not in tree:
#         count+=1
# print(tree)
#

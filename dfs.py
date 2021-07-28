graph =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False for _ in range(9)]

def dfs(graph , i ,visited):
    visited[i]=True
    print(i,"=>",end="")

    for val in graph[i]:
        if not visited[val]:
            dfs(graph,val,visited)


print(dfs(graph,1,visited))


from collections import deque
def bfs(start,graph,visited,dist):
    q = deque()
    q.append(start)
    visited[start]=True

    while q:
        v=q.popleft()
        for val in graph[v]:
            if not visited[val]:
                q.append(val)
                visited[val]=True
                dist[val] = dist[v]+1


def solution(n, edge):
    answer = 0
    graph = [[] for _  in range(n+1)]
    edge.sort()
    visited=[False]*(n+1)
    dist = [0]*(n+1)

    for val in edge:
        a = val[0]
        b = val[1]
        graph[a].append(b)
        graph[b].append(a)

    dist[1] = 1
    bfs(1,graph,visited,dist)
    return dist.count(max(dist))


# n=6
# graph = [[] for _  in range(n+1)]
# vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# visited = [False]*(n+1)
# vertex.sort()
# dist = [0]*(n+1)

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))





from collections import deque

def bfs(x,graph,visited):
    q=deque()
    q.append(x)
    while q:
        v = q.popleft()

        for val in graph[v]:
            if not visited[val]:
                q.append(val)
                visited[val]=True


def solution(n, computers):
    answer=0
    visited = [False] * n
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                computers[i][j] = 0

            elif computers[i][j] == 1:
                graph[i].append(j)


    for i in range(n):
        if not visited[i]:
            bfs(i, graph, visited)
            answer += 1


    return answer






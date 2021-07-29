from collections import deque

n,k =  map(int,input().split())
MAX = 200000
visited = [False]*(MAX+1)
dist = [0]*(MAX+1)


def bfs(n,k):
    queue = deque([n])

    while queue:
        val = queue.popleft()
        visited[val]=True

        for dis in [val-1 , val+1 , 2*val]:
            if 0<= dis <=MAX  and not visited[dis]:
                visited[dis] = True
                queue.append(dis)

                dist[dis] = dist[val]+1

    return dist[k]

print(bfs(n,k))







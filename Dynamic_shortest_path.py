graph=[
    [0,0,0,0,0],
    [0,6,7,12,5],
    [0,5,3,11,18],
    [0,7,17,3,3],
    [0,8,10,14,9]
]
dist = [[0]*5 for _ in range(5)]
print(dist)

def matrixPath(n):
    for i in range(n+1):
        for j in range(n+1):
            dist[i][j] = graph[i][j]+ max(dist[i-1][j],dist[i][j-1])


matrixPath(4)
print(dist[4][4])
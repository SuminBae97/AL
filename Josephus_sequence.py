from collections import deque

arr = deque()
n,k = map(int,input().split())
res = []
for i in range(1,n+1):
    arr.append(i)

while(len(arr)>1):
    arr.rotate(-(k-1))
    res.append(arr[0])
    del arr[0]

res.append(arr[0])

print("<",end='')
for i in res[:-1]:
    print(i,end=', ')
print(res[-1],end='')
print('>')
# 7
# 2 4
# 11 4
# 15 8
# 4 6
# 5 3
# 8 10
# 13 6
import sys
n = int(sys.stdin.readline())
storage = [0]*1001
pillar = []

for _ in range(n):
    index, height = map(int,sys.stdin.readline().split())
    storage[index]=height
    pillar.append([index,height])

max_index = storage.index(max(storage))
max_val_index = max(pillar,key = lambda x:x[0])
max_val_index = max_val_index[0]

count=0
for i in range(0,max_index+1):
    val  = max(storage[:i+1])
    count+=val

for i in range(max_val_index,max_index,-1):
    val =max(storage[:i-1:-1])
    count+=val

print(count)




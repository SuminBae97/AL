import sys
n,m = map(int,sys.stdin.readline().split())

basket=[]

for i in range(1,n+1):
    basket.append(i)


for _ in range(m):
    f,s = map(int,sys.stdin.readline().split())
    f=f-1
    s=s-1
    temp = basket[f]
    basket[f]=basket[s]
    basket[s]=temp

for val in basket:
    print(val,end=" ")





import sys
a,b,c = map(int,sys.stdin.readline().split())

length = [0]*101
f=[]
s=[]
t=[]


first,second = map(int,sys.stdin.readline().split())
length[first:second]=[1 for _ in range(first,second)]
d,e = map(int,sys.stdin.readline().split())
for i in range(d,e):
    length[i] +=1
f,g =  map(int,sys.stdin.readline().split())
for i in range(f,g):
    length[i] +=1


sum=0
for i in range(1,len(length)):
    if length[i]==0:
        pass

    elif length[i]==1:
        sum+=a*length[i]

    elif length[i]==2:
        sum+=b*length[i]

    elif length[i]==3:
        sum+=c*length[i]


print(sum)




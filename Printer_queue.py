import sys
test_case = int(sys.stdin.readline())

for i in range(test_case):
    n,f = map(int,sys.stdin.readline().split())
    priority = list(map(int,sys.stdin.readline().split()))

    p_p =[]

    for ind,val in enumerate(priority):
        p_p.append([ind,val])

    q=[]
    index=0
    cnt=0
    flag=True
    while True:
        if len(p_p)==0:
            break
        if flag:
            temp = []
            for val in p_p:
                temp.append(val[-1])
            max_val = max(temp)
        if max_val > p_p[index][1]:
            val = p_p.pop(index)
            p_p.append(val)
            flag=False

        elif max_val == p_p[index][1]:
            val = p_p.pop(index)
            cnt+=1
            q.append((val[0],cnt))
            flag=True


    for val in q:
        if val[0]==f:
            print(val[1])

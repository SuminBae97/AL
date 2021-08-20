import sys
n = int(sys.stdin.readline())
people=[]
ranking = [1]*n

for _ in range(n):
    weight, height = map(int,sys.stdin.readline().split())
    people.append([weight,height])

for index,val in enumerate(people):
    for i in range(len(people)):
        if i==index:
            continue

        else:
            c_weight = people[i][0]
            c_height = people[i][1]

            if c_weight>val[0] and c_height >val[1]:
                ranking[index]+=1

for val in ranking:
    print(val,end=" ")
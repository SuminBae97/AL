import sys
n = int(sys.stdin.readline())
cnt=0

for i in range(1,n+1):
    if i<100:
        cnt+=1

    elif i>=100 and i<1000:
        first_val = i%10
        second_val = (i%100)//10
        third_val = (i%1000)//100

        diff_1 = second_val - first_val
        diff_2 = third_val-second_val

        if diff_1==diff_2:
            cnt+=1

print(cnt)








import sys
n = int(sys.stdin.readline())



seq = list(map(int,sys.stdin.readline().split()))
dp = [1]*1001

for i in range(n):
    for j in range(i):
        if seq[i] > seq[j]:
           dp[i] = max(dp[j]+1,dp[i])
print(max(dp))
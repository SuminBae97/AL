import sys
n = int(sys.stdin.readline())

juice =[0]*10000
dp = [0]*10000

for i in range(n):
    val = (int(sys.stdin.readline()))
    juice[i] = val
    #juice.append(val)

dp[0]=juice[0]
dp[1] = juice[0]+juice[1]
dp[2] = max(dp[1],juice[0]+juice[2],juice[1]+juice[2])

for i in range(3,n):
    dp[i] = max(dp[i-1],juice[i]+dp[i-2],juice[i]+dp[i-3]+juice[i-1])

print(max(dp))
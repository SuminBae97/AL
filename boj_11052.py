import sys
n = int(input())

price = list(map(int,sys.stdin.readline().split()))
price = [0] + price
dp = [0]*(1001)
dp[1] = price[1]

for i in range(2,n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], dp[i-j] + price[j])

print(dp[n])
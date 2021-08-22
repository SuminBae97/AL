import sys
test_case = int(sys.stdin.readline())



def pado(n):
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4,n+1):
        dp[i] = dp[i-3]+dp[i-2]

    return dp[n]

for _ in range(test_case):
    val = int(sys.stdin.readline())
    print(pado(val))



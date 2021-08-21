import sys
n= int(sys.stdin.readline())


def solution(n):
    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4,n+1):

        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    return dp[n]



for i in range(n):
    val = int(sys.stdin.readline())
    print(solution(val))

import sys
sys.setrecursionlimit(10*6)

n = int(sys.stdin.readline())

arr  = [1]*(n+1)

def fibo(n,arr):
    for i in range(3,n+1):
        arr[i] = arr[i-1]+arr[i-2]

    return arr[n]

print(fibo(n,arr))
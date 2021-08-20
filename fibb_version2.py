import sys
sys.setrecursionlimit(10*6)
n = int(sys.stdin.readline())
arr =[0,1]
def dp_fibo(n):
    for i in range(2,n+1):
        arr.append(arr[i-1]+arr[i-2])

dp_fibo(n)
print(arr[n])
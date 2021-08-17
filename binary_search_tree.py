import sys

# default 값이 1000이다
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
tree =[]

def postorder(start,end):
    if start>end:
        return

    idx = start+1
    root = tree[start]

    while idx<=end:
        if tree[idx] > root:
            break
        idx+=1


    postorder(start+1,idx-1)
    postorder(idx,end)
    print(root)






while 1:
    try:
        tree.append(int(input()))
    # try에서 예외 발생시 break 실행
    except:
        break

postorder(0, len(tree) - 1)
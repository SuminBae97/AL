import sys
n = int(sys.stdin.readline())

stack =[]

for _ in range(n):
    vps = sys.stdin.readline()
    stack=[]
    for i in range(len(vps)-1):
        if vps[i]=="(":
            stack.append(vps[i])

        elif vps[i]==')':
            try:
                if stack[-1] == "(":
                    stack.pop()


            except IndexError:
                stack.append(")")

    if len(stack)>=1:
        print("NO")
    else:
        print("YES")















# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys
stack=[]
n= int(sys.stdin.readline())

def push(x):
    stack.append(x)

def pop():
    if len(stack)<=0:
        print(-1)
    else:
        val = stack.pop()
        print(val)

def size():
    if len(stack)<=0:
        print(0)

    else:
        print(len(stack))


def empty():
    if len(stack)==0:
        print(1)
    else:
        print(0)

def top():
    if len(stack)==0:
        print(-1)

    else:
        print(stack[-1])

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0]=='push':
        stack.append(int(command[1]))

    elif command[0]=="top":
        top()


    elif command[0]=="size":
        size()

    elif command[0]=="empty":
        empty()

    elif command[0]=="pop":
        pop()

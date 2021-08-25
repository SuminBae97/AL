import sys

while True:
    st = input()
    stack=[]
    is_empty = True


    if st==".":
        break

    for s in st:
        if s == "(" or s == "[":
            stack.append(s)
            is_empty = False

        elif s==")" and is_empty==True:
            stack.append(s)
            is_empty=False
        elif s=="]" and is_empty==True:
            stack.append(s)
            is_empty=False

        elif s==")" and is_empty==False:
            try:
                if stack[-1]=="(":
                    stack.pop(-1)
                    if len(stack)==0:
                        is_empty=True
                else:
                    stack.append(s)

            except IndexError:
                stack.append(s)
        elif s == "]" and is_empty == False:
            try:
                if stack[-1] == "[":
                    stack.pop(-1)
                    if len(stack) == 0:
                        is_empty = True
                else:
                    stack.append(s)

            except IndexError:
                stack.append(s)

        elif s=="":
            stack.append(s)
            is_empty=False


    if len(stack)==0 or is_empty==True:
        print("yes")
    else:
        print("no")

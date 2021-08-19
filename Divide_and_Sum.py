
import sys
n = int(sys.stdin.readline())
#몇자리수?
#len_of_str=len(str(n))


answer=[]
for i in range(1,n+1):
    words = []
    len_of_str = len(str(i))

    while len_of_str != 0:
        a = (i % (10 ** (len_of_str))) // (10 ** (len_of_str - 1))
        words.append(a)
        len_of_str -= 1

    len_sum = sum(words)
    val = i+len_sum

    if val==n:
        answer.append(i)


if len(answer)==0:
    print(0)
else:
    val =min(answer)
    print(val)










import sys
n = int(sys.stdin.readline())

tri = []
for _ in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    tri.append(temp)

for i in range(1,len(tri)):
    for j in range(len(tri[i])):
        if j==0:
            tri[i][j] = tri[i-1][j] + tri[i][j]

        elif j==(len(tri[i])-1):
            tri[i][j] =tri[i-1][j-1] + tri[i][j]

        else:
            tri[i][j] = max(tri[i][j]+tri[i-1][j-1], tri[i][j]+tri[i-1][j])

print(max(tri[n-1]))

#
#
#
# # answer = tri[0][0]
# # index = 1
# # start = 0
# # while index!=n:
# #     answer+=max(tri[index][start],tri[index][start+1])
# #     start = tri[index].index(max(tri[index][start],tri[index][start+1]))
# #     #층수 높이기
# #     index+=1
# #
# # print(answer)
#
#

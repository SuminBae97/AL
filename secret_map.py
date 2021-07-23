def solution(n, arr1, arr2):
    answer = []
    temp1 = []
    temp2 = []

    for val in arr1:
        bi = format(val, 'b')
        t = ["0" for _ in range(n - len(bi))]
        t = ''.join(t)
        a = list(t + bi)
        temp1.append(a)

    for val in arr2:
        bi = format(val, 'b')
        t = ["0" for _ in range(n - len(bi))]
        t = ''.join(t)
        a = list(t + bi)
        temp2.append(a)

    for list_1 in temp1:

        for i in range(len(list_1)):
            list_1[i] = int(list_1[i])

    for list_1 in temp2:
        for i in range(len(list_1)):
            list_1[i] = int(list_1[i])

    result = [[a + b for a, b in zip(i, j)] for i, j in zip(temp1, temp2)]

    for i in range(len(result)):
        for j in range(len(result[i])):
            if result[i][j] == 2 or result[i][j] == 1:
                result[i][j] = "#"
            else:
                result[i][j] = " "
    for val in result:
        r = ''.join(val)
        answer.append(r)
    return answer
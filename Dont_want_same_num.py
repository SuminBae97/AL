def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(len(arr)):

        try:
            if arr[i] == arr[i + 1]:
                continue
            answer.append(arr[i + 1])

        except IndexError:
            break

    return answer


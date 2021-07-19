def solution(numbers):
    answer = []
    arr = set()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            arr.add(numbers[i]+numbers[j])
    answer = list(arr)
    answer.sort()

    return answer

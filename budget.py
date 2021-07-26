def solution(d, budget):
    d.sort()
    count = 0
    for val in d:
        budget = budget - val
        if budget >=0:
            count+=1
        else:
            break
    return count
print(solution([1,3,2,5,4],9))
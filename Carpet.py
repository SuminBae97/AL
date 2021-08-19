
def solution(brown,yellow):
    answer=[]
    n = brown + yellow
    nums = []
    for i in range(1, n + 1):
        if n % i == 0:
            nums.append(i)

    for index, vals in enumerate(nums):
        if len(answer)!=0:
            break
        if vals < 3:
            continue
        elif vals >= 3:
            #answer.append(vals)
            for j in range(index, len(nums)):
                if nums[j] * vals == n and ((vals-2)*(nums[j]-2))>=yellow:
                    answer.append(nums[j])
                    answer.append(vals)
                    break



    answer.sort(reverse=True)
    return answer


#print(solution(10,2))

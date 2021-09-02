
def solution(phone_book):
    answer=True
    dic={}
    for pNumber in phone_book:
        dic[pNumber]=1

    for pNumber in phone_book:
        temp=""
        for num in pNumber:
            temp+=num

            if temp in dic and temp!=pNumber:
                answer=False
    return answer







print(solution(["119", "97674223", "1195524421"]))


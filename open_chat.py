
idDict={}

def solution(record):
    answer=[]
    loglist=[]
    for val in record:
        a = val.split(" ")
        if a[0]=="Leave":
            loglist.append([a[1], "님이 나갔습니다."])

        elif a[0]=="Enter":
            idDict[a[1]]=a[2]
            loglist.append([a[1] ,"님이 들어왔습니다."])

        elif a[0]=="Change":
            idDict[a[1]]=a[2]


    for val in loglist:
        val[0] = idDict[val[0]]
        answer.append(val[0]+val[1])

    return answer
record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))

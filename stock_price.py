def solution(prices):
    answer = [0]*len(prices)
    stock_len = len(prices)

    for i in range(stock_len):
        count=0
        for j in range(i+1,stock_len):
            if prices[i] <=prices[j]:
                count+=1
        answer[i]=count

    return answer


#print(solution([1, 2, 3, 2, 3]))
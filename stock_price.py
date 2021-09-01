def solution(prices):
    answer = [0]*len(prices)
    stock_len = len(prices)

    for i in range(stock_len):
        for j in range(i+1,stock_len):
            if prices[i] <=prices[j]:
                answer[i]+=1
            else:
                answer[i]+=1
                break

    return answer
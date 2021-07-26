import heapq

def solution(scoville, K):
    answer = 0
    count = 0
    heap = []
    for val in scoville:
        heapq.heappush(heap,val)


    i=0
    while heap[0]<K:
        try:
            f = heapq.heappop((heap))
            s = heapq.heappop((heap))
            new_sco = f + (2 * s)
            heapq.heappush(heap, new_sco)

        except IndexError:
            return -1

        count+=1

    return count

print(solution([1, 2, 3, 9, 10, 12],7))
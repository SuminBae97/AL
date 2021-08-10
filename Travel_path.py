



from collections import defaultdict


def solution(tickets):
    answer = []

    graph = defaultdict(list)
    for dept, arrv in sorted(tickets):
        graph[dept].append(arrv)
    def dfs(dept):
        while graph[dept]:
            dfs(graph[dept].pop(0))

        answer.append(dept)

    dfs("ICN")
    return answer[::-1]





# #tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
#
# graph={}
# places=set()
# visited={}
# answer=[]
#
# for val in tickets:
#     start = val[0]
#     arrival = val[1]
#     places.add(start)
#     places.add(arrival)
#     #graph.append({start:[arrival]})
#     if start in graph.keys():
#         graph[start].append(arrival)
#     else:
#         graph[start] = [arrival]
# for val in places:
#     visited[val]=False
#
# for val in graph.values():
#     val.sort()

def dfs(start,visited,answer,graph):
    visited[start]=True
    #print(start)
    answer.append(start)
    for i in graph[start]:
        try:
            if not visited[i] or len(graph[i]) != 2:
                graph[start].pop(0)
                dfs(i,visited,answer,graph)
        except KeyError:
            return


#dfs("ICN")
#print(answer)


def solution(tickets):
    graph = {}
    places = set()
    visited = {}
    answer = []

    for val in tickets:
        start = val[0]
        arrival = val[1]
        places.add(start)
        places.add(arrival)
        # graph.append({start:[arrival]})
        if start in graph.keys():
            graph[start].append(arrival)
        else:
            graph[start] = [arrival]
    for val in places:
        visited[val] = False

    for val in graph.values():
        val.sort()

    dfs("ICN",visited,answer,graph)
    return answer

#print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
#print(solution(tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
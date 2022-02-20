import collections
import heapq  # 우선순위 큐 구현을 위함


def solution(n, graph):

    result=0

    temp=[]

    key_data = collections.deque(graph.keys())


    for data in graph:
        temp = graph[data]
        for x in temp:
            if x in key_data:
                for y in graph[x]:
                    if y not in graph[data]:
                        graph[data].append(y)

    num_req = n-1

    while key_data:
        checker = False
        k = key_data.popleft()

        if len(graph[k])==num_req:
            result+=1
            for kk in key_data:
                if k not in graph[kk]:
                    graph[kk].append(k)
        else:
            key_data.append(k)

        for kk in key_data:
            if len(graph[kk]) == num_req:
                checker = True

        if not checker:
            break


    return result


if __name__ == '__main__':

    n = 5

    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

    graph = collections.defaultdict(list)

    for i in range(len(results)):
        graph[results[i][1]].append(results[i][0])

    result = solution(n, graph)

    print(result)
import heapq

def dijkstraMap(start):
    dis = [0xffffff] * (n + 1)
    dis[start] = 0
    q = [[0, start]]
    while q:
        k, u = heapq.heappop(q)
        if k > dis[u]: continue
        for w, v in graph[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(q, [dis[v], v])

    return dis

def bfs(startMap, midMap, a, b):
    res = float('inf')
    for mid in range(1,n+1):
        sToMid = startMap[mid]
        midToA = midMap[mid][a]
        midToB = midMap[mid][b]
        cost = sToMid+midToA+midToB
        if res>cost:
            res = cost

    return res

def solution(n, s, a, b, graph):

    # mid까지 최단거리를 구한다. s -> a,b를 제외한 나머지 노드로의 거리
    # mid->a // mid->b를 구한다.

    startDij = dijkstraMap(s)
    
    midDij = []

    for i in range(0, n+1):
        if i==0:
            midDij.append([])
            continue
        midDij.append(dijkstraMap(i))

    res = bfs(startDij, midDij, a, b)

    return res

if __name__ == '__main__':

    n, s, a, b = 6, 4, 6, 2
    data = [[4, 1, 10], [3, 5, 24], [5, 6, 2], 
            [3, 1, 41], [5, 1, 24], [4, 6, 50], 
            [2, 4, 66], [2, 3, 22], [1, 6, 25]]

    graph = [[] for _ in range(n+1)]
    
    for i in range(len(data)):
        u, v, w = data[i]
        graph[u].append([w, v])
        graph[v].append([w, u])

    res = solution(n,s,a,b,graph)

    print(res)
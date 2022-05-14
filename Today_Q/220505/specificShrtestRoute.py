from collections import defaultdict
import heapq
import sys

def dijkstra(start, end):
    dis = [0xffffff] * (N + 1)
    dis[start] = 0
    q = [[0, start]]
    while q:
        k, u = heapq.heappop(q)
        if k > dis[u]: continue
        for w, v in graph[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(q, [dis[v], v])

    return dis[end]


if __name__ == '__main__':

    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append([w, v])
        graph[v].append([w, u])

    stop1, stop2 = map(int, sys.stdin.readline().split())

    # 1 -> stop1 -> stop2 -> N
    path1 = dijkstra(1, stop1) + dijkstra(stop1, stop2) + dijkstra(stop2, N)
    # 1 -> stop2 -> stop1 -> N
    path2 = dijkstra(1, stop2) + dijkstra(stop2, stop1) + dijkstra(stop1, N)

    if path1 >= 0xffffff and path2 >= 0xffffff:
        print(-1)
    else:
        print(min(path1, path2))
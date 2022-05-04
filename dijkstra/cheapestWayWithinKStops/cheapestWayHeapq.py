import collections
import heapq  # 우선순위 큐 구현을 위함


def dijkstra(n, flights, src, dst, K):
    graph = collections.defaultdict(list)

    for u,v,w in flights:
        graph[u].append((v,w))
    print("data",graph)
    queue = [(0, src, K)]

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        price, node, k = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

        if node == dst:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            return price

        if k>=0:
            for v,w in graph[node]:
                alt = price + w  # 해당 노드를 거쳐 갈 때 거리
                heapq.heappush(queue, (alt, v, k-1))  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

    return -1


if __name__ == '__main__':

    n = 5
    src = 0
    dst = 4
    k = 3

    times = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1],[3, 4, 1]]

    result = dijkstra(n, times, src, dst, k)

    print(f'{result}')
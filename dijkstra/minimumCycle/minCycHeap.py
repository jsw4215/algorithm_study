import collections
import heapq  # 우선순위 큐 구현을 위함
import sys


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
    distances[start] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

        if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue

        for new_destination, new_distance in graph[current_destination]:
            distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
            if new_destination == start:
                lst.append(distance)

            if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

    pass


if __name__ == '__main__':

    input = sys.stdin.readline
    INF = int(1e9)

    n, m = map(int, input().split())

    graph = collections.defaultdict(list)

    nodeList = set()

    lst = []

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        nodeList.add(a)

    for start in nodeList:
        dijkstra(graph, start)

    if lst:
        print(f'{min(lst)}')
    else:
        print(-1)
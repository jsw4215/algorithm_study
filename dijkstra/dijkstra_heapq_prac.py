import heapq  # 우선순위 큐 구현을 위함


def dijkstra(graph, start):

    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [start, distance[start]])

    while queue:
        now_destination, now_distance = heapq.heappop(queue)

        if distance[now_destination] < now_distance:
            continue

        for new_dest, new_dist in graph[now_destination].items():
            cost = new_dist + now_distance
            if cost < distance[new_dest]:
                distance[new_dest] = cost
                heapq.heappush(queue, [new_dest, cost])

    return distance


if __name__ == '__main__':

    graph = {
        'A': {'B': 8, 'C': 1, 'D': 2},
        'B': {},
        'C': {'B': 5, 'D': 2},
        'D': {'E': 3, 'F': 5},
        'E': {'F': 1},
        'F': {'A': 5}
    }

    result = dijkstra(graph, 'A')

    print(f'{result}')
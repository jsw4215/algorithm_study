import sys


def dijkstra(times, start, n):

    graph = [None]*(n+1)

    for i in times:
        if graph[i[0]] is None:
            graph[i[0]] = [[i[1],i[2]]]
        else:
            graph[i[0]].append([i[1],i[2]])


    visited = [False]*(n+1)
    distance = [INF]*(n+1)

    def get_nearest():
        idx = 0
        min = INF
        for i in range(len(distance)):
            if visited[i] is False and min > distance[i]:
                min = distance[i]
                idx = i

        return idx


    def algo():

        distance[start] = 0

        for _ in range(n):

            now = get_nearest()
            visited[now] = True

            if graph[now] is None:
                continue

            for dest_dist in graph[now]:
                cost = distance[now] + dest_dist[1]

                if distance[dest_dist[0]] > cost:
                    distance[dest_dist[0]] = cost


    algo()

    distance.pop(0)

    result = max(distance)

    print(f'{result}')

    return distance


if __name__ == '__main__':

    INF = int(1e9)

    n = 4
    k = 2

    times = [
        [2,1,1],
        [2,3,1],
        [3,4,1]
    ]

    result = dijkstra(times, k, n)
    print(f'{result}')
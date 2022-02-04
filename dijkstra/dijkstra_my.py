import sys


def dijkstra(graph, start):

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

            for dest_dist in graph[now]:
                cost = distance[now] + dest_dist[1]

                if distance[dest_dist[0]] > cost:
                    distance[dest_dist[0]] = cost


    algo()

    return distance


if __name__ == '__main__':

    input = sys.stdin.readline
    INF = int(1e9)

    n, m = 6, 11
    start = 1

    graph = [
        [],
        [[2,2],[3,5],[4,1]],
        [[3,3],[4,2]],
        [[2,3],[6,5]],
        [[3,3],[5,1]],
        [[3,1],[6,2]],
        []
    ]

    result = dijkstra(graph, 1)
    print(f'{result}')
import sys


def dijkstra(legs, n, dep, dest, k):

    graph = [None]*(n+1)
    INF = int(1e9)

    queue = []

    for i in legs:
        if graph[i[0]] is None:
            graph[i[0]] = [[i[1],i[2]]]
        else:
            graph[i[0]].append([i[1],i[2]])

    visited = [False]*(n+1)
    distance = [[INF,None] for _ in range(n)]

    def get_nearest():
        idx = 0
        min = INF

        for i in range(len(distance)):
            if visited[i] is False and min > distance[i][0]:
                min = distance[i][0]
                idx = i

        return idx

    via = 0

    def algo():

        distance[dep][0] = 0
        distance[dep][1] = 0

        for _ in range(n):

            now = get_nearest()
            visited[now] = True

            if graph[now] is None:
                continue

            for dest_dist in graph[now]:
                cost = distance[now][0] + dest_dist[1]

                if distance[dest_dist[0]][0] > cost:
                    if distance[dest_dist[0]][1] is None or distance[now][1] <= k:
                        distance[dest_dist[0]][0] = cost
                        distance[dest_dist[0]][1] = distance[now][1] + 1
                    if dest_dist[0] == dest and distance[dest_dist[0]][1]-1 == k:
                        return cost

    result = algo()

    return result


if __name__ == '__main__':

    input = sys.stdin.readline


    n = 3
    src = 0
    dst = 2
    k = 1

    times = [[0,1,100],[1,2,100],[0,2,500]]

    result = dijkstra(times, n, src, dst, k)
    print(f'{result}')
import sys


def dijkstra(graph, start):

    visited = [False] * (n + 1)  # 방문처리 기록용
    distance = [INF] * (n + 1)  # 거리 테이블용

    def smallest_cost():
        min = INF
        idx = 0
        for i in range(len(distance)):
            if visited[i] is False and distance[i]!=INF:
                if min > distance[i]:
                    min = distance[i]
                    idx = i
        return idx

    def algo(start):
        #시작지점 처리
        visited[start] = True
        distance[start] = 0

        #시작노드에서 가는 지점들의 거리와 비용 업데이트
        for dest_cost in graph[start]:
            distance[dest_cost[0]] = dest_cost[1]

        for _ in range(n-1):

            now = smallest_cost()
            visited[now] = True

            #해당 노드에서 뻗어나가는 길, 비용 계산 후 업데이트
            for dest_dist in graph[now]:

                cost = distance[now] + dest_dist[1]
                #목적지가 방문처리 전이고, 거리가 재산정 비용보다 크면
                if distance[dest_dist[0]] > cost:
                    distance[dest_dist[0]] = cost

    algo(start)

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
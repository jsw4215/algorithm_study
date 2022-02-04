#시간초과
import collections
import sys


def dijkstra():

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


    def algo(start):

        visited[start] = True
        distance[start] = 0

        #시작노드에서 가는 지점들의 거리와 비용 업데이트
        for dest_cost in graph[start]:
            distance[dest_cost[0]] = dest_cost[1]

        for _ in range(n-1):

            now = get_nearest()
            visited[now] = True

            for dest_dist in graph[now]:
                cost = distance[now] + dest_dist[1]

                if dest_dist[0] == start:
                    nonlocal result
                    if result>cost:
                        result = cost

                if distance[dest_dist[0]] > cost:
                    distance[dest_dist[0]] = cost

    result=INF

    for node in nodeList:
        visited = [False] * (n + 1)
        distance = [INF] * (n + 1)
        algo(node)

    if result==INF:
        return -1
    else:
        return result


if __name__ == '__main__':

    input = sys.stdin.readline
    INF = int(1e9)

    n, m = map(int, input().split())

    graph = collections.defaultdict(list)

    nodeList = set()

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        nodeList.add(a)

    result = dijkstra()
    print(f'{result}')
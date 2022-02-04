import sys


def dijkstra(graph, n):


    visited = [[False for _ in range(n)] for _ in range(n)]  # 방문처리 기록용
    distance = [[-1 for _ in range(n)] for _ in range(n)] # 거리 테이블용

    def smallest_cost():
        min = INF
        idx = []
        for i in range(n):
            for j in range(n):
                if visited[i][j] is False and distance[i][j]!=-1:
                    if min > distance[i][j]:
                        min = distance[i][j]
                        idx = [i,j]
        return idx

    def algo():

        x=0
        y=0
        px = [-1,1,0,0]
        py = [0,0,-1,1]

        #시작지점 처리
        visited[0][0] = True
        distance[0][0] = graph[0][0]

        #시작노드에서 가는 지점들의 거리와 비용 업데이트
        for i in range(4):
            nx = x + px[i]
            ny = y + py[i]
            if n > nx >= 0 and n > ny >= 0:
                cost = graph[nx][ny] + graph[x][y]
                distance[nx][ny] = cost

        while True:

            now = smallest_cost()

            if not now:
                break

            x = now[0]
            y = now[1]

            visited[x][y] = True

            # 시작노드에서 가는 지점들의 거리와 비용 업데이트
            for i in range(4):
                nx = x + px[i]
                ny = y + py[i]
                if visited[nx][ny] is not True and n > nx >= 0 and n > ny >= 0:
                    cost = graph[nx][ny] + graph[x][y]
                    if distance[nx][ny]==-1:
                        distance[nx][ny] = cost
                    elif distance[nx][ny] > cost:
                        distance[nx][ny] = cost

    algo()

    return distance


if __name__ == '__main__':

    input = sys.stdin.readline
    INF = int(1e9)

    n = 3

    graph = [
        [5,5,4],
        [3,9,1],
        [3,2,7]
    ]

    result = dijkstra(graph, n)

    print(f'{result}')
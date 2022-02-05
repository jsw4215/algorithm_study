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
                cost = graph[nx][ny] + distance[x][y]
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
                if  n > nx >= 0 and n > ny >= 0 and visited[nx][ny] is not True:
                    cost = graph[nx][ny] + distance[x][y]
                    if distance[nx][ny] == -1:
                        distance[nx][ny] = cost
                    elif distance[nx][ny] > cost:
                        distance[nx][ny] = cost

    algo()

    return distance[n-1][n-1]


if __name__ == '__main__':

    input = sys.stdin.readline
    INF = int(1e9)

    graph = []
    i = 0

    while True:

        n = int(input())

        if n==0:
            break

        for _ in range(n):
            row = list(map(int, input().split()))
            graph.append(row)

        result = dijkstra(graph, n)
        i+=1
        print(f'Problem {i}: {result}')
        graph=[]
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = 4
m = 7
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

temp = [
    [1, 2, 4],
    [1, 4, 6],
    [2, 1, 3],
    [2, 3, 7],
    [3, 1, 5],
    [3, 4, 4],
    [4, 3, 2]
]

for i in range(m):
    row = temp[i]
    graph[row[0]][row[1]] = row[2]

for k in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            if graph[x][y] > graph[x][k] + graph[k][y]:
                graph[x][y] = graph[x][k] + graph[k][y]

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

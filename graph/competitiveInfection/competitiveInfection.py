from collections import deque

def solution(grid):
    px = [-1, 1, 0, 0]
    py = [0, 0, -1, 1]


    def dfsInfection():
        count = 0
        queue = deque(virus)

        #이렇게 정렬하면 틀렸다고 나오고
        #sorted(queue, key=lambda x: x[0])

        while queue:
            if count == sec:
                break

            for _ in range(len(queue)):

                temp = queue.popleft()
                degree = temp[0]
                x = temp[1]
                y = temp[2]

                for i in range(4):
                    nx = px[i] + x
                    ny = py[i] + y

                    # 조건들
                    if 0 <= nx < N and 0 <= ny < N:
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = grid[x][y]
                            queue.append((grid[x][y], nx, ny))
            count+=1

        return grid[target_x-1][target_y-1]

    #정렬을 이렇게 하니 틀리지 않았다.
    virus.sort()

    print(dfsInfection())


if __name__ == '__main__':
    N, max_num = map(int, input().split())
    _map = []
    virus = []
    for i in range(N):
        temp = list(map(int, input().split()))
        _map.append(temp)
        for j in range(N):
            if _map[i][j] != 0:
                virus.append((_map[i][j], i, j))

    sec, target_x, target_y = map(int, input().split())

    solution(_map)

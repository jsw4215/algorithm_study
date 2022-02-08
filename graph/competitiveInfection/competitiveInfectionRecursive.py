from collections import deque


def solution(grid):
    result = 0
    px = [-1, 1, 0, 0]
    py = [0, 0, -1, 1]
    rows = len(grid)
    cols = len(grid[0])
    count=0

    def recur(temp):

        degree = temp[0]
        x = temp[1]
        y = temp[2]

        for i in range(4):
            nx = px[i] + x
            ny = py[i] + y
            # 조건들

            if nx < 0 or ny < 0 or nx >= cols or ny >= rows:
                continue

            if grid[ny][nx] == 0:
                grid[ny][nx] = degree


    def dfsInfection():

        queue = deque([])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    temp = grid[i][j]
                    queue.append([temp, i, j])

        sorted(queue, key=lambda x: x[0])

        while queue:
            recur(queue.popleft())

        nonlocal count
        count += 1

        if count==sec:
            return

        dfsInfection()



    dfsInfection()

    return grid[target_y-1][target_x-1]


if __name__ == '__main__':

    lines, max_num = map(int, input().split())
    _map = []
    for _ in range(lines):
        temp = list(map(int, input().split()))
        _map.append(temp)

    sec, target_x, target_y = map(int, input().split())

    result = solution(_map)

    print(f'{result}')

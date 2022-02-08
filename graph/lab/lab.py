import copy
from collections import deque


def solution(grid):

    result = 0
    px = [-1,1,0,0]
    py = [0,0,-1,1]
    rows = len(grid)
    cols = len(grid[0])

    def dfsInfection():

        testGrid = copy.deepcopy(grid)
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if testGrid[i][j] == 2:
                    queue.append([i, j])

        while queue:
            temp = queue.popleft()
            x = temp[1]
            y = temp[0]

            for i in range(4):
                nx = px[i] + x
                ny = py[i] + y
                # 조건들

                if nx < 0 or ny < 0 or nx >= cols or ny >= rows:
                    continue

                if testGrid[ny][nx] == 0:
                    testGrid[ny][nx] = 2
                    queue.append([ny, nx])

        clean = 0

        #for문 2개할것을 1개로 가능하다 이렇게
        for i in range(rows):
            clean+=testGrid[i].count(0)

        nonlocal result



        result = max(result, clean)

    def wall(cnt):

        if cnt == 3:
            dfsInfection()

            #여기 return 까먹었었음
            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    grid[i][j] = 1
                    wall(cnt + 1)
                    grid[i][j] = 0

    wall(0)

    return result


if __name__ == '__main__':
    n = 4
    m = 6
    map = [
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 2],
        [1, 1, 1, 0, 0, 2],
        [0, 0, 0, 0, 0, 2]
    ]

    result = solution(map)

    print(f'{result}')

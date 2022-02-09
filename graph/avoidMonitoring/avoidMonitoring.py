import copy
import sys
from collections import deque


def solution(grid):

    result = "NO"
    px = [-1,1,0,0]
    py = [0,0,-1,1]
    rows = len(grid)
    cols = len(grid[0])

    def dfsInfection():
        nonlocal result
        testGrid = copy.deepcopy(grid)
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if testGrid[i][j] == "T":
                    queue.append([i, j])

        while queue:
            temp = queue.popleft()
            x = temp[1]
            y = temp[0]

            for i in range(4):
                nx = x
                ny = y
                while result == "NO":
                    nx = px[i] + nx
                    ny = py[i] + ny
                    # 조건들

                    if nx < 0 or ny < 0 or nx >= cols or ny >= rows:
                        break

                    if testGrid[ny][nx] == "X":
                        testGrid[ny][nx] = "T"
                    elif testGrid[ny][nx] == "S":
                        return
                    elif testGrid[ny][nx] == "W":
                        break
        #모든 조건 통과시
        result = "YES"

    def wall(cnt):

        if cnt == 3:
            dfsInfection()

            #여기 return 까먹었었음
            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if result=="YES":
                    break
                if grid[i][j] == "X":
                    grid[i][j] = "W"
                    wall(cnt + 1)
                    grid[i][j] = "X"

    wall(0)

    return result


if __name__ == '__main__':
    with open('avoidMonitoring_testcase.txt') as f:
        sys.stdin = f
        input = sys.stdin.readline
        N = int(input())

        table = []
        for i in range(N):
            table.append(list(input().split()))

        result = solution(table)

        print(f'{result}')

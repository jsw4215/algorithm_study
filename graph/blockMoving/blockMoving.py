import copy
from collections import deque


def solution(grid):
    result = "NO"
    px = [-1, 1, 0, 0]
    py = [0, 0, -1, 1]

    # x좌표에
    ctrClockWise = [[[1, 0], [0, 0]], [[0, 1], [0, 0]]]
    # y좌표에
    clockWise = [[[0, 0], [1, 0]], [[0, 0], [0, -1]]]

    rows = len(grid)
    cols = len(grid[0])
    robot = [[0, 0], [0, 1]]

    # 회전시 무빙
    # 반시계 = robot[0][0]+1,robot[0][1] => robot[0][0], robot[0][1]+1
    # 시계 = robot[1][0]+1,robot[1][1] => robot[1][0], robot[1][1]-1
    # robot = [x,y] // x=[0,0] y=[0,1]이라 했을 때
    # 아래 -> 우 = robot[[x[0]+1,y[0]],y]
    def dfsRobot():
        nonlocal result
        testGrid = copy.deepcopy(grid)

        left = robot[0]
        right = robot[1]

        for i in range(4):
            nx = left
            ny = right
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
        # 모든 조건 통과시
        result = "YES"

    dfsRobot()

    return result


if __name__ == '__main__':
    table = [
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0]
    ]

    result = solution(table)

    print(f'{result}')

import sys


def solution(gridX, gridY, str):
    # if len(str)==0:
    #     return 0

    pivot = 1
    starting_point_x = -1
    starting_point_y = -1

    # start

    x = starting_point_x
    y = starting_point_y

    px = [-1, 1, 0, 0]
    py = [0, 0, -1, 1]

    for char in str:
        if char == 'U':
            if x == -1 and y ==-1:
                x=4
                y=5
                gridY[x][y]=pivot
            else:
                x = x + px[0]
                y = y + py[0]
                if 0 <= x < 10 and 0 <= y < 10:
                    gridY[x][y] = pivot
                else:
                    x = x - px[0]
                    y = y - py[0]
        elif char == 'D':
            if x == -1 and y ==-1:
                x=5
                y=5
                gridY[x][y]=pivot
            else:
                x = x + px[1]
                y = y + py[1]
                if 0 <= x < 10 and 0 <= y < 10:
                    gridY[x][y] = pivot
                else:
                    x = x - px[1]
                    y = y - py[1]
        elif char == 'L':
            if x == -1 and y ==-1:
                x=5
                y=4
                gridX[x][y] = pivot
            else:
                x = x + px[2]
                y = y + py[2]
                if 0 <= x < 10 and 0 <= y < 10:
                    gridX[x][y] = pivot
                else:
                    x = x - px[2]
                    y = y - py[2]
        elif char == 'R':
            if x == -1 and y ==-1:
                x=5
                y=5
                gridX[x][y] = pivot
            else:
                x = x + px[3]
                y = y + py[3]
                if 0 <= x < 10 and 0 <= y < 10:
                    gridX[x][y] = pivot
                else:
                    x = x - px[3]
                    y = y - py[3]

    result = 0

    for i in gridX:
        result += sum(i)
    for i in gridY:
        result += sum(i)

    return result


if __name__ == '__main__':

    gridX = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    gridY = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    n = str(sys.stdin.readline())

    result = solution(gridX, gridY, n)

    print('result : ' + str(result))


def solution(grid):
    INF = int(1e9)
    result = []
    rows = len(grid)
    cols = len(grid[0])
    checker_board = [[False for _ in range(cols)] for _ in range(rows)]
    distance_board = [[INF for _ in range(cols)] for _ in range(rows)]

    px = [-1, 1, 0, 0]
    py = [0, 0, -1, 1]
    count = 0

    def smallest(x, y):

        min = INF
        temp = []

        px = [-1, 1, 0, 0]
        py = [0, 0, -1, 1]

        for i in range(4):
            nx = px[i] + x
            ny = py[i] + y

            # 조건들
            if nx < 0 or ny < 0 or nx >= cols or ny >= rows or checker_board[ny][nx]:
                continue
            print('[nx] :' + str(nx) + ', [ny]: ' + str(ny))
            if grid[ny][nx] == 0:
                continue

            if grid[ny][nx] < min:
                min = grid[ny][nx]
                temp = [ny, nx]

            if distance_board[ny][nx] > distance_board[y][x] + grid[ny][nx]:
                distance_board[ny][nx] = grid[ny][nx] + distance_board[y][x]

        return temp


    def maze(x, y):
        checker_board[y][x] = True

        tempYX = smallest(x,y)

        if not tempYX:
            return

        maze(tempYX[1], tempYX[0])


    distance_board[0][0] = grid[0][0]
    maze(0, 0)

    return distance_board[n-1][m-1]


if __name__ == '__main__':

    n = 5
    m = 6
    iceBoarder = [
        [1,0,1,0,1,0],
        [1,1,1,1,1,1],
        [0,0,0,0,0,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1]
    ]

    result = solution(iceBoarder)

    print(f'{result}')
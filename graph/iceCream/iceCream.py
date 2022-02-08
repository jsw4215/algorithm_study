def solution(grid):

    result = []
    rows = len(grid)
    cols = len(grid[0])
    px = [-1, 1, 0, 0]
    py = [0, 0, -1, 1]
    count = 0

    def isLandDfs(x, y):

        grid[y][x] = 1

        for i in range(4):
            nx = px[i] + x
            ny = py[i] + y
            # 조건들

            if nx < 0 or ny < 0 or nx >= cols or ny >= rows:
                continue
            print('[nx] :' + str(nx) + ', [ny]: ' + str(ny))
            if grid[ny][nx] == 1:
                continue

            isLandDfs(nx, ny)

    for x in range(cols):
        for y in range(rows):

            if grid[y][x] == 1:
                continue

            count += 1

            isLandDfs(x, y)

    return count


if __name__ == '__main__':

    n = 4
    m = 5
    iceBoarder = [
        [0,0,1,1,0],
        [0,0,0,1,1],
        [1,1,1,1,1],
        [0,0,0,0,0]
    ]

    result = solution(iceBoarder)

    print(f'{result}')
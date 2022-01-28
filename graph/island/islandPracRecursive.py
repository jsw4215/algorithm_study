def solution(grid):

    result = []
    rows = len(grid)
    cols = len(grid[0])
    px = [-1,1,0,0]
    py = [0,0,-1,1]
    count = 0

    def isLandDfs(x, y):

        grid[y][x] = "0"
        for i in range(4):
            nx = px[i] + x
            ny = py[i] + y
            # 조건들

            if nx < 0 or ny < 0 or nx >= cols or ny >= rows:
                print("e")
                continue
            print('[nx] :' + str(nx) + ', [ny]: ' + str(ny))
            if grid[ny][nx] == "0":
                continue


            isLandDfs(nx,ny)


    for x in range(cols):
        for y in range(rows):

            if grid[y][x] == "0":
                continue

            count+=1

            isLandDfs(x,y)

    return count

if __name__ == '__main__':

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    result = solution(grid)

    print('result : ' + str(result))
def solution(grid):

    result = []
    rows = len(grid)
    cols = len(grid[0])
    px = [-1,1,0,0]
    py = [0,0,-1,1]
    count = 0
    stack = []

    for x in range(rows):
        for y in range(cols):

            if grid[x][y] == "0":
                continue
            count+=1
            stack.append((x,y))
            while stack:
                x, y = stack.pop()

                grid[x][y] = "0"

                for i in range(4):
                    nx = px[i]+x
                    ny = py[i]+y
                    print("nx : " + str(nx) + ", ny : " + str(ny))
                    if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny]=="0":
                        continue

                    stack.append((nx,ny))

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
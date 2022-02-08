from collections import deque


def solution(grid, n, min, max):

    result = []
    rows = len(grid)
    cols = len(grid[0])
    px = [-1,1,0,0]
    py = [0,0,-1,1]
    count = 0
    check_grid = [[True for _ in range(cols)] for _ in range(rows)]
    cnt_nation = 0
    tot = 0

    def nationDfs(x, y):

        nonlocal tot
        nonlocal cnt_nation

        queue = deque([[x,y]])

        while queue:
            poi = queue.popleft()
            for i in range(4):
                nx = px[i] + poi[1]
                ny = py[i] + poi[0]

                # 조건들
                if nx < 0 or ny < 0 or nx >= cols or ny >= rows:
                    continue

                print('[nx] :' + str(nx) + ', [ny]: ' + str(ny))
                if min <= abs(grid[poi[1]][poi[0]] - grid[ny][nx]) <= max and check_grid[ny][nx]:
                    tot += grid[ny][nx]
                    check_grid[ny][nx] = False
                    cnt_nation += 1

                    queue.append([ny, nx])

        print("tot : " + str(tot))
        #한 싸이클 이후 하루 카운트
        nonlocal count
        count += 1


        #연합 인구 계산
        union = tot//cnt_nation

        #연합 인구 업데이트 후 변수 초기화
        cnt_nation = 0
        tot = 0

        #싸이클중 False 표시된 국가 인구 union으로 업데이트
        for i in range(cols):
            for j in range(rows):
                if check_grid[j][i] == False:
                    grid[j][i] = union
                    check_grid[j][i] = None


        nationDfs(0,0)


    # check_grid[0][0] = False
    # tot += grid[0][0]
    # cnt_nation += 1
    nationDfs(0,0)

    return count

if __name__ == '__main__':

    # n = 2
    # min = 20
    # max = 50
    #
    # grid = [
    #     [50, 30],
    #     [20, 40]
    # ]

    n = 2
    min = 40
    max = 50

    grid = [
        [50, 30],
        [20, 40]
    ]

    result = solution(grid, n , min, max)

    print('result : ' + str(result))
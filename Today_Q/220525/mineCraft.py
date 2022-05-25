import sys

def solution(grid):
    ans = int(1e9)
    
    for i in range(257):
        remove = 0
        addition = 0
        for j in range(n):
            for k in range(m):
                if grid[j][k]<i:
                    addition += (i-grid[j][k])
                else:
                    remove += (grid[j][k]-i)
        #블럭의 갯수가 모자랄 경우
        if remove+b < addition:
            continue
        time = 2*remove + addition
        if time<=ans:
            ans = time
            height = i

    print(ans, height)
    pass

if __name__ == '__main__':

    input = sys.stdin.readline

    n,m,b = map(int, input().split())

    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    solution(grid)



import collections
import sys

#바이러스가 들어있는 좌표 가져오기
def getVirusXY(space):

    virus = []

    for x in range(len(space)):
        for y in range(len(space[x])):
            if space[x][y] != 0:
                virusNum = space[x][y]
                virus.append([virusNum,x,y])
    virus.sort()
    return virus

#좌표를 바탕으로 dx,dy 주변 전염
def spreadingVirus(virusArr):
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    newVir = []

    for virus in virusArr:
        for d in range(4):
            virusNum = virus[0]
            nx = virus[1] + dx[d]
            ny = virus[2] + dy[d]

            if 0<=nx<n and 0<=ny<n and space[nx][ny]==0:
                space[nx][ny] = virusNum
                newVir.append([virusNum,nx,ny])

    return newVir

def solution():

    virusArr = getVirusXY(space)
    cnt = s

    while cnt:
        cnt-=1
        virusArr = spreadingVirus(virusArr)

    return space[x-1][y-1]

if __name__ == '__main__':
    
    input = sys.stdin.readline

    n, k = map(int, input().split())

    space = []

    for _ in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        space.append(temp)

    s, x, y = map(int, input().split())

    res = solution()

    print(res)
from collections import deque
import sys

def getClouds(cloudsMap):
    newClouds = []

    for x in range(n):
        for y in range(n):
            #fix if [x,y] not in clouds:
            if not cloudsMap[x][y]:
                if space[x][y]>=2:

                    # if [x,y] in clouds:
                    #     continue

                    space[x][y]-=2
                    newClouds.append([x,y])

    return newClouds

def moveClouds(vector, clouds):
    dx = [0,-1,-1,-1,0,1,1,1]
    dy = [-1,-1,0,1,1,1,0,-1]

    for cloud in clouds:
        cloud[0] = (n + cloud[0] + (dx[vector[0]-1]*vector[1]))%n
        cloud[1] = (n + cloud[1] + (dy[vector[0]-1]*vector[1]))%n
        #비내리기
        space[cloud[0]][cloud[1]]+=1
    return clouds

def copyWater(clouds):
    dx = [-1,-1,1,1]
    dy = [-1,1,1,-1]

    for cloud in clouds:
        for d in range(4):
            nx = cloud[0] + dx[d]
            ny = cloud[1] + dy[d]

            if 0<=nx<n and 0<=ny<n and space[nx][ny]:
                space[cloud[0]][cloud[1]]+=1

def cloudsMapping(cloudsIdx):
    cloudsMap = [[False]*n for _ in range(n)]
    for x,y in cloudsIdx:
        cloudsMap[x][y]=True
    return cloudsMap

def solution():
    #구름의 이동
    #1. 구름 위치 pointer 표현 ㅇ
    #2. 물의 양 map 표현 ㅇ
    #3. 움직임 함수 ㅇ
    #4. 구름아래 물 +1 ㅇ
    #5. 구름이 사라진다
    #6. 대각선 위치에 물이 있다면 있는 위치만큼 +0~4
    #7. 물의양 2 이상인 곳에 새로운 구름 생성, 물-2, 구름이 사라진 곳 은 아님 ㅇ
    global space
    cloudsIdx = [[n-2,0],[n-2,1],[n-1,0],[n-1,1]]
    #fix 구름 map으로 매칭하도록 변경
    cloudsMap = [[False]*n for _ in range(n)]

    for x,y in cloudsIdx:
        cloudsMap[x][y]=True

    while moves:

        vector = moves.popleft()

        cloudsIdx = moveClouds(vector, cloudsIdx)

        cloudsMap = cloudsMapping(cloudsIdx)

        copyWater(cloudsIdx)

        cloudsIdx = getClouds(cloudsMap)

    res = 0

    for line in space:
        res+=sum(line)

    return res

if __name__ == '__main__':

    n, m = map(int, sys.stdin.readline().split())

    space = []
    moves = deque([])

    for _ in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        space.append(temp)

    for _ in range(m):
        temp = list(map(int, sys.stdin.readline().split()))
        moves.append(temp)

    res = solution()

    print(res)
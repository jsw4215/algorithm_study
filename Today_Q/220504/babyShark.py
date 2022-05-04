from collections import deque
import sys

def findShark():
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if lines[x][y]==9:
                lines[x][y]=0
                return [x,y]

def findNearestTarget(sharkPosition, fishBowl):
    #어항의 모든 위치에 도달하는 가장 가까운 경우의 수 map
    distance = [[sys.maxsize]*n for _ in range(n)]
    distance[sharkPosition[0]][sharkPosition[1]] = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque([sharkPosition])
    targetList = []
    curDist = sys.maxsize
    global time
    global sharkSize

    while q:

        now = q.popleft()
        newTime = distance[now[0]][now[1]]+1

        if curDist < newTime:
            break

        for d in range(4):

            nx = now[0] + dx[d]
            ny = now[1] + dy[d]

            if 0<=nx<n and 0<=ny<n and fishBowl[nx][ny]<=sharkSize:
                
                if distance[nx][ny] > newTime:
                
                    distance[nx][ny] = newTime
                    q.append([nx,ny])
                
                    if 0<fishBowl[nx][ny]<sharkSize:
                        curDist = newTime
                        targetList.append([nx,ny])

    if targetList:
        time+=curDist
    return targetList

def solution():
    #다음 먹이찾기
    #1. 거리가 가장 가까운 먹이
    #2. 여러마리라면 list[x][y]에서 x값이 적은 것
    #3. x도 같다면 y가 적은 것
    #4. 없다면 엄마 호출
    sharkPosition = findShark()
    eaten = 0
    
    global time
    global sharkSize

    while True:

        nearestTarget = findNearestTarget(sharkPosition, lines)

        if len(nearestTarget)==0:
            break

        nearestTarget.sort()
        target = nearestTarget[0]

        #상어 옮기기
        lines[target[0]][target[1]] = 0
        sharkPosition = target
        eaten+=1

        if sharkSize == eaten:
            sharkSize+=1
            eaten=0


    return time

if __name__ == '__main__':

    n = int(sys.stdin.readline())

    lines = []

    for _ in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        lines.append(temp)

    time = 0
    sharkSize = 2
    res = solution()

    print(res)
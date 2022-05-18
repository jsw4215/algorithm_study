import sys

def checkTime(tempGrid):
    time=0
    #총 필요한 시간
    for i in range(len(tempGrid)):
        for j in range(len(tempGrid[i])):
            if tempGrid[i][j]<0:
                time+=abs(tempGrid[i][j])
            elif tempGrid[i][j]>0:
                time+=(tempGrid[i][j])*2
    return time

def solution(grid, keeps):

    avg = 0
    tempGrid = [i[:] for i in grid]
    
    for line in grid:
        tmp = max(line)
        avg = max(tmp, avg)
        # tmp = sum(line)/len(line)
        # if avg:
        #     avg = (tmp+avg)/2
        # else:
        #     avg+=tmp

    #avg = tmp
    prev = 0
    while avg:
        #평균으로 맞출 시, 필요한 블록 갯수
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                tempGrid[i][j]-=avg

        temp = 0
        for line in tempGrid:
            temp+=sum(line)

        now = checkTime(tempGrid)
        if now>prev:
            avg+=1
            tempGrid = [i[:] for i in grid]
            break

        if keeps+temp<0:
            prev = now
            avg-=1
            tempGrid = [i[:] for i in grid]

        else:
            now = checkTime(tempGrid)
            break
    
    return now, avg

if __name__ == '__main__':

    input = sys.stdin.readline

    grid = []

    n,m,b = map(int, input().split())

    for i in range(n):
        temp = list(map(int, input().split()))
        grid.append(temp)

    t, a = solution(grid, b)

    print(t, a)

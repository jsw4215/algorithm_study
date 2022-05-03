import sys

def getRipe():
    
    ripe = []

    for x in range(len(boxes)):
        for y in range(len(boxes[x])):
            for z in range(len(boxes[x][y])):
                if boxes[x][y][z] == 1:
                    ripe.append([x,y,z])

    return ripe

def setRipe(ripe):

    checker = []

    for x,y,z in ripe:
        
        for d in range(6):
            nx, ny, nz = x+dx[d], y+dy[d], z+dz[d]
            if 0<=nx<h and 0<=ny<n and 0<=nz<m:
                if boxes[nx][ny][nz] == 0:
                    checker.append([nx,ny,nz])
                    boxes[nx][ny][nz] = 1
    return checker

def allRipeChecker():
    for x in range(len(boxes)):
        for y in range(len(boxes[x])):
            for z in range(len(boxes[x][y])):
                if boxes[x][y][z] == 0:
                    return False
    return True

def solution():
    
    res = -1
    check = getRipe()
    while check:
        check = setRipe(check)
        res+=1
    
    if allRipeChecker():
        return res
    else:
        return -1

if __name__ == '__main__':
    
    input = sys.stdin.readline

    m, n, h = map(int, input().split())

    dx = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dz = [0,0,0,0,-1,1]

    boxes = []

    for j in range(0, h):
        box = []
        for i in range(0, n):
            temp = list(map(int, sys.stdin.readline().split()))
            box.append(temp)
        boxes.append(box)

    res = solution()

    print(res)
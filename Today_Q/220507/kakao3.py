from collections import deque

def xArr(H, W):
    x = [0]*W

    for i in range(1, H):
        x+=[i]

    x += [W-1]*W

    for i in range(H-1, 0, -1):
        x+=[i]
    
    return x

def yArr(W, H):
    y = []

    for i in range(0, W):
        y+=[i]

    y += [W-1]*H
    
    for i in range(H-1, 0, -1):
        y+=[i]
    
    y += [0]*H

    return y


def calc(table, H, W, N):
    temp = table[:]

    x = xArr(H, W)

    y = yArr(W, H)
    
    print(x, y)

    x = deque(x)
    y = deque(y)
    x.rotate(N)
    y.rotate(N)

    

    for i in range(W-1, 0, -1):
        temp[0][i] = table[x[i]][y[i]]

    for i in range(H):
        for j in range(W):
            table[i][j] = table[x[i]]
            print(table)

    return table

def solution(rc, operations):
    H = len(rc)
    W = len(rc[0])
    operations = deque(operations)
    ret = deque(rc)

    order = 0
    while operations:
        action = operations.popleft()

        if order>=0:
            if action[0]=="R":
                order+=1
            else:
                calc(rc, H, W, order)
                order=-1
        if order<=0:
            if action[0]=="S":
                order-=1
            else:
                ret.rotate(abs(order))
                order=1
    
    return list(ret)

if __name__ == '__main__':

    rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    operations = ["Rotate", "ShiftRow"]

    res = solution(rc, operations)

    print(res)
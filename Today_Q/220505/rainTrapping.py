import sys

def rightToLeft(height):

    temp = [0]*w
    temp[-1] = height[-1]

    for i in range(len(height)-2, -1, -1):
        temp[i] = max(temp[i+1], height[i])

    return temp

def leftToRight(height):

    temp = [0]*w
    temp[0] = height[0]

    for i in range(1, len(height)):
        temp[i] = max(temp[i-1], height[i])

    return temp


def solution():
    #1. 좌->우
    #2. 우->좌
    #3. min(좌,우) - height

    l = leftToRight(height)
    r = rightToLeft(height)
    res = []
    for i in range(w):
        res[i] = min(r[i],l[i]) - height[i]

    return sum(res)

if __name__ == '__main__':

    h, w = map(int, sys.stdin.readline().split())

    height = list(map(int, sys.stdin.readline().split()))

    res = solution()

    print(res)
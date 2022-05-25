import sys

def findSquare(r,c,res,x,y):
    if x<2 or y<2:
        return res

    area = x*y//4
    nr=0
    nc=0

    if r<x//2:
        #1,2번 square
        if c<y//2:
            #1번 square
            res+=0
            nr=r
            nc=c
        else:
            res+=area
            nr=r
            nc=c-y//2
    else:
        #3,4번 square
        if c<y//2:
            #3번 square
            res+=area*2
            nr=r-x//2
            nc=c
        else:
            res+=area*3
            nr=r-x//2
            nc=c-y//2

    nx=x//2
    ny=y//2

    return findSquare(nr, nc, res, nx, ny)

def solution():


    res = 0
    res = findSquare(r,c,res,x,y)
    print(res)
    pass

if __name__ == '__main__':

    input = sys.stdin.readline

    n,r,c = map(int, input().split())
    x = 2**n
    y = 2**n
    solution()



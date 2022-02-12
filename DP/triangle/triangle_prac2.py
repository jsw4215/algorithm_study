import sys

with open('testcase_triangle.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline

    INF = int(1e9)

    N = int(input())

    tri = []

    for i in range(N):
        tri.append(list(map(int, input().split())))

    accu = []
    temp = []
    for i in range(N):
        temp=[]
        for j in range(i+1):
            temp.append(INF)
        accu.append(temp)

    def tri_dp2(x, y):

        if x<0 or y<0 or x>=N or y>x:
            return 0

        if accu[x][y]!=INF:
            #이부분 주의!!!! accu가 아닌 tri[x][y] 리턴하면 안됨
            return accu[x][y]

        accu[x][y] = tri[x][y] + max(tri_dp2(x - 1, y - 1), tri_dp2(x - 1, y))

        return accu[x][y]


    for i in range(N):
        tri_dp2(N - 1, i)

    print(accu)
    print(max(accu[N-1]))



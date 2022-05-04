import sys

with open('testcase_triangle.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline

    INF = int(1e9)

    N = int(input())

    tri = []

    for i in range(N):
        tri.append(list(map(int, input().split())))

    memo = [[INF] * (i + 1) for i in range(N)]
    memo[0][0] = tri[0][0]

    def tri_dp(x,y):

        if not (0<=x<N and 0<=y<=x):
            return 0

        if memo[x][y] != INF:
            return memo[x][y]

        memo[x][y] = tri[x][y] + max(tri_dp(x-1,y-1), tri_dp(x-1,y))

        return memo[x][y]

    for i in range(N) :
        test = tri_dp(N-1,i)

    print(f'{max(memo[N-1])}')






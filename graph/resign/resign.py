import sys

with open('resign_testcase.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline

    INF = int(1e9)

    N = int(input())

    table = []

    for i in range(N):
        table.append(list(map(int, input().split())))

    max_pay = 0

    def resign_dp(idx, pay):
        global max_pay

        if idx>=N:
            if max_pay < pay:
                max_pay = pay
            return

        for i in range(2):
            if i==1:
                if idx+table[idx][0] > N:
                    return
                resign_dp(idx + table[idx][0], pay + table[idx][1])
            else:
                resign_dp(idx+1, pay)


    resign_dp(0, 0)

    print(f'{max_pay}')






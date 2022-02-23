import sys


def sol(lst):

    lst = sorted(lst, key=lambda x: x[0])

    x = lst[int(n/2)][0]

    lst = sorted(lst, key=lambda x: x[1])

    y = lst[int(n/2)][1]

    res = 0

    for i in range(n):
        res+=abs(x-lst[i][0])+abs(y-lst[i][1])

    print(res)

    pass


if __name__ == '__main__':

    with open('testcase_14400.txt') as f:
        sys.stdin = f
        input = sys.stdin.readline

        n = int(input())

        lst = []

        for _ in range(n):
            lst.append(list(map(int,input().split())))


        result = sol(lst)
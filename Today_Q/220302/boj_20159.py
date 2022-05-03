import sys
from collections import deque


def sol(lst):

    result = 0

    def dfs_stack(x):
        nonlocal result
        tot =0
        queue = deque(lst[:])
        turn = True
        cnt=0

        while queue:

            if cnt==x:
                card = queue.pop()
            else:
                card = queue.popleft()

            if turn:
                tot+=card
                turn = False
            else:
                turn = True

            cnt += 1

        if tot > result:
            result = tot

        pass

    dfs_stack(-1)

    for i in range(len(lst)-1):
        dfs_stack(i)

    print(f'{result}')

    pass


if __name__ == '__main__':

    with open('testcase_20159.txt') as f:
        sys.stdin = f
        input = sys.stdin.readline

        n = int(input())

        lst = []

        lst = list(map(int,input().split()))

        result = sol(lst)
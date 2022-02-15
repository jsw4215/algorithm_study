from collections import deque


def solution(s):
    dq = deque([])

    result = 0

    for i in range(1,s+1):
        dq.append(i)

    while len(dq)>1:
        dq.popleft()
        temp=dq.popleft()
        dq.append(temp)


    return dq.pop()


if __name__ == '__main__':

    n = int(input())

    res = solution(n)

    print(res)
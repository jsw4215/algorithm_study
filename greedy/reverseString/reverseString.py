import sys


def solution(n):

    temp0 = n.split("1")
    temp0 = ' '.join(temp0).split()
    temp1 = n.split("0")
    temp1 = ' '.join(temp1).split()

    result = min(len(temp1),len(temp0))

    print(result)


if __name__ == '__main__':

    n = sys.stdin.readline()

    solution(n)

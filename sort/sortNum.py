import sys


def solution(l):

    l.sort()

    for i in range(len(l)):
        print(l[i])

    pass

if __name__ == '__main__':

    n = int(sys.stdin.readline())
    l = []
    for _ in range(n):
        age = input()
        age = int(age)
        l.append(age)

    solution(l)

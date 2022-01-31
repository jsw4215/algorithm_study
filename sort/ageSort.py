import sys


def solution(l):

    l = sorted(l, key = lambda x:x[0])

    for i in range(len(l)):
        print(l[i][0],l[i][1])

    pass

if __name__ == '__main__':

    n = int(sys.stdin.readline())
    l = []
    for _ in range(n):
        age, name = input().split()
        age = int(age)
        l.append([age, name])

    solution(l)

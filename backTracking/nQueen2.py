import sys


def check(line, vstd):

    for i in range(line):
        if vstd[i] == vstd[line] or abs(line - i) == abs(vstd[line] - vstd[i]):
            return False

    return True


def solution (n):

    count=0
    visited=[0]*n

    def setQueen(line):


        if line>=n:
            nonlocal count
            count+=1
            return

        for i in range(n):
            visited[line] = i
            if check(line, visited):
                setQueen(line+1)

    setQueen(0)

    print(count)
    pass

if __name__ == '__main__':

    n = int(input())

    result = solution(n)
import sys

def solution(test):

    res = []

    for case in test:
        temp = ""
        R = int(case[0])
        S = list(case[1])
        for s in S:
            temp+=(s*R)
        res.append(temp)

    return res

if __name__ == '__main__':

    input = sys.stdin.readline

    n = int(input())

    test = []

    for i in range(n):
        s = list(input().split())
        test.append(s)
    
    result = solution(test)

    for res in result:
        print(res)

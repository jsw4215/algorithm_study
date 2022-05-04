from collections import deque
import sys

def checkWithPart(part, s, idx):

    if part*(len(s)//idx) == s:
        return True

    # for i in range(idx, len(s), idx):
    #     if not s[i:i+idx]==part:
    #         return False
    return False

def checkWithMeasure(s, measure):

    for m in measure:
        part = s[:m]

        if checkWithPart(part, s, m):
            return len(s)//m

    return 1

def getMeasure(num):
    measure = []
    for i in range(1, num+1):
        if num % i == 0:
            measure.append(i)
    
    return measure

def solution():
    #0. 문자열 길이의 약수 구하기
    #1. 문자열을 자른다.

    res = []

    for _str in arr:
        measure = getMeasure(len(_str))
        res.append(checkWithMeasure(_str, measure))

    return res

if __name__ == '__main__':

    arr = []

    while True:
        temp = sys.stdin.readline().rstrip()
        if temp=='.':
            break
        arr.append(temp)

    res = solution()

    for i in res:
        print(i)
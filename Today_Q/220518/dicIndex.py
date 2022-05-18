import collections
import sys

def solution(S):
    l = dict()
    for i in range(ord('a'), ord('z')+1):
        l[chr(i)]=-1


    for idx in range(len(S)):
        if l[S[idx]]==-1:
            l[S[idx]]=idx

    return l.values()

if __name__ == '__main__':

    input = sys.stdin.readline

    s = input().strip('\n')

    result = solution(s)

    print(*result)

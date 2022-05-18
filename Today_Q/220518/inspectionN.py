import collections
import sys

def solution(l):
    res = 0
    for item in l:
        res+=item**2
    return res%10

if __name__ == '__main__':

    input = sys.stdin.readline
    s = list(map(int,input().split()))
    result = solution(s)    
    print(result)

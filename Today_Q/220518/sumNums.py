import sys

def solution(s):
    return ord(s)

if __name__ == '__main__':

    input = sys.stdin.readline

    s = input().strip('\n')

    result = solution(s)

    print(result)

import sys

def solution(l):
    one = l[0]
    two = l[1]

    one = int(''.join(list(reversed(list(one)))))
    two = int(''.join(list(reversed(list(two)))))

    return max(one,two)

if __name__ == '__main__':

    input = sys.stdin.readline
    s = list(map(str,input().split()))
    result = solution(s)    
    print(result)

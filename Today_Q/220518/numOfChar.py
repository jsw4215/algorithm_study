import collections
import sys

def solution(S):
    l = collections.defaultdict(int)
    for char in S:
        l[char.upper()]+=1

    res = max(l.values(), key=lambda a:a)
    res = [k for k,v in l.items() if max(l.values()) == v]
    if len(res)==1:
        return res[0]
    else:
        return "?"

if __name__ == '__main__':

    input = sys.stdin.readline

    s = input().strip('\n')

    result = solution(s)

    print(result)

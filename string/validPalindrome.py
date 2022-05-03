import collections


def solution(s):
    
    strs = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    
    return True

if __name__ == '__main__':
    n = "A man, a plan, a canal: Panama"

    result = solution(n)

    print('result : ' + str(result))
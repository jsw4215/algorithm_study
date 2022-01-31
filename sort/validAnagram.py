def solution(s, t):

    print(sorted(s))

    return sorted(s) == sorted(t)


if __name__ == '__main__':

    s = "anagram"
    t = "nagaram"

    result = solution(s, t)
    print(f'result: {result}')
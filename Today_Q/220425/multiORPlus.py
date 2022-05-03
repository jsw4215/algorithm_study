def solution(s):

    answer = 0

    for i in range(len(s)):
        x=int(s[i])
        if x<2 or not answer:
            print("+",s[i])
            answer+=x
        else:
            print("*",s[i])
            answer*=x

    print("res",answer)
    pass


if __name__ == '__main__':

    n = "567"

    palinList = solution(n)
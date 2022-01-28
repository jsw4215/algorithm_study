def isPalindrome(str):
    # moom
    # mom

    # i: in order (0
    # j: in reverse order (2

    # 초기값 예외처리
    # 1) 대소문자를 구분하지 않음
    # 2) 영문자와 숫자만 대상으로 함 (isalnum(), alphabet+number)
    #  1-1) 영문자와 숫자인 문자열만 타겟으로 보겠다 (만약 특수기호가 들어가면 False)
    #  1-2) 만약에 특수기호가 들어가면 특수기호는 무시하고 보겠다
    #       mo,m => palindrome

    str = str.lower()

    i = 0
    j = - i - 1
    isPalin = True
    while True:
        if i + 1 == len(str) // 2 or j + 1 == len(str) // 2:
            break

        if not str[i].isalnum():
            i += 1
            break
        if not str[j].isalnum():
            j -= 1
            break
        if str[i] != str[j]:
            isPalin = False
            break

        i += 1
        j -= 1

    return isPalin


if __name__ == "__main__":
    # mom, rotator, ...
    palin = isPalindrome("erhfdg")
    print(palin)

def longest_palindrome(s):

    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    #효율성을 위한 빠른 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    #일반적인 경우
    for i in range(len(s)-1):
        result = max(result,
                     expand(i,i+1),
                     expand(i,i+2),
                     key=len)

    return result


if __name__ == '__main__':

    n = "asdfesdfarotaatorasdfasdfasdf"


    palin = longest_palindrome(n)

    print('List : ' + str(palin))
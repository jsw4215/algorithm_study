def solution(s):

    onelist = s.split('1')
    onelist = ' '.join(onelist).split()
    zerolist = s.split('0')
    zerolist = ' '.join(zerolist).split()

    print("onelist",onelist)
    print("zerolist",zerolist)

    return min(len(onelist),len(zerolist))

if __name__ == '__main__':

    n = "000111000"

    res = solution(n)

    print("res",res)
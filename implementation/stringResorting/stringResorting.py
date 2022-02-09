def solution(n):

    temp=0
    strTemp=[]
    for i in n:
        if i.isdecimal():
            temp+=int(i)
        else:
            strTemp.append(i)
    strTemp.sort()
    _str = ''.join(strTemp)
    _str+=str(temp)

    print(_str)


if __name__ == '__main__':

    n = "K1KA5CB7"

    solution(n)

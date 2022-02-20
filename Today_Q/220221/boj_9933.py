import sys


def sol(lst):

    result=''
    res_size=0

    for pw in lst:
        if pw[::-1] in lst :
            res_size = len(pw)
            result = pw[res_size//2]


    print(res_size, result)

    pass


if __name__ == '__main__':



    n = int(input())

    lst = []

    for _ in range(n):
        lst.append(input())


    result = sol(lst)
def solution(n,lst):

    lst.sort()

    target = 1

    for i in lst:
        if target < i:
            break
        target += i

    print(target)


if __name__ == '__main__':

    n = 5
    lst = [3,2,1,1,9]

    solution(n,lst)

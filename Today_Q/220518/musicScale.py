import sys

def solution(l):

    checker = True
    ascTrueDscFalse = None

    for i in range(len(l)-1):
        if (l[i]-1)==l[i+1]:
            ascTrueDscFalse = True
            continue
        if (l[i]+1)==l[i+1]:
            ascTrueDscFalse = False
            continue
        checker = False
        ascTrueDscFalse = None
        break

    if checker:
        if not ascTrueDscFalse:
            return "ascending"
        if ascTrueDscFalse:
            return "descending"
    elif not checker:
        return "mixed"

if __name__ == '__main__':

    input = sys.stdin.readline

    l = list(map(int, input().split()))

    result = solution(l)

    print(result)

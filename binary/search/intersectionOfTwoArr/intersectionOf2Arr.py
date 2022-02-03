import bisect


def solution(l1, l2):

    l2.sort()
    result = set()

    for i in l1:
        j = bisect.bisect_left(l2, i)
        if len(l2) > 0 and len(l2) > j and i == l2[j]:
            result.add(i)

    return result

if __name__ == '__main__':

    l1 = [1,2]
    l2 = [1,1]

    result = solution(l1, l2)

    print(str(result))
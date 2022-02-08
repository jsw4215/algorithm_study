from bisect import bisect_left, bisect_right


def solution(x, lst):

    left = bisect_left(lst, x)
    right = bisect_right(lst, x)

    return right-left

if __name__ == '__main__':

    x = int(input())
    lst = [1,1,2,2,2,2,3]

    result = solution(x, lst)

    print('result : ' + str(result))
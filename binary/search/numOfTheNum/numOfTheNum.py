from bisect import bisect_left, bisect_right


def solution(x, lst):

    low=bisect_left(lst, x , x)
    high=bisect_right(lst, x, x)

    result = high - low


    return result

if __name__ == '__main__':

    x = int(input())
    lst = [1,1,2,2,2,2,3]

    result = solution(x, lst)

    print('result : ' + str(result))
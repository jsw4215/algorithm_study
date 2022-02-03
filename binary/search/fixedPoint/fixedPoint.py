from bisect import bisect_left

def solution(n, l1):

    result = -1

    def bin_search():
        nonlocal result

        left = 0
        right = len(l1)-1

        while left <= right :

            mid = (left + right)//2

            if mid > l1[mid]:
                left = mid+1
            elif mid < l1[mid]:
                right = mid-1
            else:
                result = mid
                break

    bin_search()

    return result


if __name__ == '__main__':

    n = 5
    l1 = [-15,-6,1,3,7]

    result = solution(n, l1)

    print('result : ' + str(result))
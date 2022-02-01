from bisect import bisect_left

def solution(numOfRiceCake, requested, lst):

    result = 0

    def bin_search(left, right):

        nonlocal result

        while left < right:
            result=0
            mid = (left + right) // 2

            for rc in lst:
                if rc > mid:
                    result += (rc-mid)

            if result > requested:
                left = mid+1
            elif result < requested:
                right = mid-1
            else:
                return mid


    left = 0
    right = max(lst)

    result = bin_search(left, right)

    return result


if __name__ == '__main__':

    nm = list(map(int, input().split()))
    numOfRC = nm[0]
    requestLen = nm[1]
    lstOfRC = [19, 15, 10, 17]

    result = solution(numOfRC, requestLen, lstOfRC)

    print('result : ' + str(result))
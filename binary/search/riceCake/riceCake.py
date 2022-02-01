from bisect import bisect_left

def solution(numOfRiceCake, requested, lst):

    arr = []
    result = []

    for i in range(len(lst)):
        idx = bisect_left(arr, lst[i])
        arr.insert(idx, lst[i])

    def bin_search(left, right):

        mid = (left + right) // 2

        node = arr[mid]

        if requested > node:
            left = mid + 1
            result.append(node - requested)
        elif requested < node:
            right = mid -1
            result.append(0)
        else:
            result.append(0)
            return result

        bin_search(left, right)

    left = 0
    right = numOfRiceCake - 1

    result = bin_search(left, right)





    return result

if __name__ == '__main__':

    nm = list(map(int, input().split()))
    numOfRC = nm[0]
    requestLen = nm[1]
    lstOfRC = [19, 15, 10, 17]

    result = solution(numOfRC, requestLen, lstOfRC)

    print('result : ' + str(result))
def merging(arr, left, mid, right):

    temp = []
    l, h = left, mid

    while l < mid and h < right:
        if arr[l] < arr[h]:
            temp.append(arr[l])
            l += 1
        else:
            temp.append(arr[h])
            h += 1

    while l < mid:
        temp.append(arr[l])
        l += 1
    while h < right:
        temp.append(arr[h])
        h += 1

    for i in range(left, right):
        arr[i] = temp[i - left]

    return arr


def mergeSort(arr, left, right, lv):

    if left < right:

        mid = left + (right-left)//2

        mergeSort(arr, left, mid, lv+1)
        mergeSort(arr, mid + 1, right, lv+1)

        arr = merging(arr, left, mid, right)

    return arr


if __name__ == '__main__':

    n = [3,30,34,5,9]

    result = mergeSort(n, 0, len(n) - 1, 0)
    print(f'result: {result}')

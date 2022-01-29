def partition(arr, left, right):

    pivot = arr[right]

    i = left-1

    for j in range(left, right):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1], arr[right] = arr[right], arr[i+1]

    return i+1


def quickSort(arr, left, right):

    if left < right:

        pivot = partition(arr, left, right)

        quickSort(arr, left, pivot-1)
        quickSort(arr, pivot+1, right)

    return arr


if __name__ == '__main__':

    n = [3,30,34,5,9]

    result = quickSort(n, 0, len(n)-1)
    print(f'result: {result}')

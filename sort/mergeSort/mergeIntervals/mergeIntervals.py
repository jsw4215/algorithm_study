def mergeSort(arr):

    arr = sorted(arr, key=lambda x: x[0])

    result = []

    i=0
    while i<len(arr):
        temp = []
        if i==len(arr)-1:
            result.append(arr[i])
            break

        if arr[i][1]>=arr[i+1][0]:
            temp = [arr[i][0], max(arr[i+1][1],arr[i][1])]
            result.append(temp)
            i+=1
        else:
            result.append(arr[i])
        i+=1

    return result


if __name__ == '__main__':

    n = [[1,3],[2,6],[8,10],[15,18]]

    result = mergeSort(n)
    print(f'result: {result}')

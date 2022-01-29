def mergeArr(arr, left, mid, right, lv):
    #빈 배열로 시작해 마지막에 뒤에 붙여주는 방법은, 우측 배열을 정렬시 left~right 범위에 포함되지 않는
    #배열 부분을 무시하게 되므로 전체 배열을 복사하여 인덱스값에 붙여넣는 방식으로 한다.
    result = arr[:]
    part1 = left
    part2 = mid+1
    #index값 별도로 선언
    index = left
    #두 배열의 첫 요소를 비교하여 더 적은 값 순으로 result에 붙여주고,
    #두 배열 중 하나가 범위를 넘어갈 시, 종료
    while part1<=mid and part2<=right:
        if arr[part1]<=arr[part2]:
            result[index] = arr[part1]
            part1 += 1
        else:
            result[index] = arr[part2]
            part2 += 1
        index+=1

    #두 배열 중 탐색되지 않은 부분이 남아있는 배열을 찾아 붙여주기
    if part1<=mid:
        while part1<=mid:
            result[index] = arr[part1]
            part1+=1
            index+=1

    if part2<=right:
        while part2<=right:
            result[part2] = arr[part2]
            part2+=1
            index+=1

    #해당 left ~ right에 포함되지 않은, 배열 뒷 부분 붙여주기 - 에러
    # for i in range(right+1,len(arr)):
    #     result.append(arr[i])

    return result


def mergeSort(arr, left, right, lv):

    while left < right:

        mid = left + (right - left) // 2

        arr = mergeSort(arr, left, mid, lv+1)
        arr = mergeSort(arr, mid+1, right, lv+1)

        arr = mergeArr(arr, left, mid, right, lv+1)
        #한번 합치면 break 해줘야함
        break

    return arr


if __name__ == '__main__':

    n = [5,3,2,4,1]

    result = mergeSort(n, 0, len(n) - 1, 0)
    print(f'result: {result}')

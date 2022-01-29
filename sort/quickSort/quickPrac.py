def quickPrac(nums, left, right, lv):
    #***이것을 통해 불필요한 재귀를 제거한다.
    if left>=right:
        return nums

    #좌측편향 피봇으로 시작하는 퀵소트
    pivot = left
    left = pivot+1
    start = pivot
    end = right
    while left <= right:
        #pivot보다 left가 작으면 계속 탐색(left+=1), 아니면 멈춤
        while left<=end and nums[left] <= nums[pivot]:
            left += 1
        #pivot보다 right가 크면 계속 탐색
        while right>start and nums[right] >= nums[pivot]:
            right -= 1
        if left > right:
            nums[right], nums[pivot] = nums[pivot], nums[right]
        else:
            nums[left], nums[right] = nums[right], nums[left]


    nums = quickPrac(nums, start, right-1, lv+1)
    nums = quickPrac(nums, right+1, end, lv+1)

    return nums


if __name__ == '__main__':

    n = [5,4,2,1,3,422,4,4,3,6,7,2,6,8,4,36,8,9,95467]

    result = quickPrac(n, 0, len(n)-1, 0)
    print(f'result: {result}')

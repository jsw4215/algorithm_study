def solution(target, nums):

    result = []

    def bi_search(idx):
        nonlocal result
        x = idx
        left = idx+1
        right = len(nums)-1

        while left<=right:
            mid = (left + right) //2

            if nums[x] + nums[mid] > target:
                right = mid-1
            elif nums[x] + nums[mid] < target:
                left = mid+1
            else:
                temp = [x, mid]
                result.append(x)
                result.append(mid)
                break

        return result

    for i in range(len(nums)):
        result=bi_search(i)

    return result

if __name__ == '__main__':

    target = 9
    nums = [2,7,11,15]

    result = solution(target, nums)

    print('result : ' + str(result))
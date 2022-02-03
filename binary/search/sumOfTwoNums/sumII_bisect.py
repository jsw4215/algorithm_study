import bisect


def solution(target, nums):

    for idx, n in enumerate(nums):
        expected = target-n
        i = bisect.bisect_left(nums, expected, idx+1)
        if i<len(nums) and nums[idx] + nums[i] == target:
            return [idx+1,i+1]

if __name__ == '__main__':

    target = 9
    nums = [2,7,11,15]

    result = solution(target, nums)

    print('result : ' + str(result))
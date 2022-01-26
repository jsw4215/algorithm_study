def solution(nums):

    del nums[3]
    nums.remove(500)

    return nums


if __name__ == '__main__':

    nums = [100,200,300,400,500]

    result = solution(nums)

    print('result : ' + str(result))
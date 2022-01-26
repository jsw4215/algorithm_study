def solution(nums):

    nums.insert(2,1000)

    return nums


if __name__ == '__main__':

    nums = [200,100,300]

    print(type(nums))

    a = 'p'
    print(type(a))


    result = solution(nums)

    print('result : ' + str(result))
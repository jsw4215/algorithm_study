def largestNum(nums):
    if sum(nums)==0:
        return "0"

    for i in range(len(nums)):

        for j in range(i+1,len(nums)):
            if int(str(nums[i])+str(nums[j]))<int(str(nums[j])+str(nums[i])):
                nums[j], nums[i] = nums[i], nums[j]

    result=""

    for num in nums:
        result += str(num)


    return result


if __name__ == '__main__':

    n = [3,30,34,5,9]

    result = largestNum(n)
    print(f'result: {result}')

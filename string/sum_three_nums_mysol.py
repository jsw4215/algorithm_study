def sum_three_num_func(nums):
    result = []

    for pivot in range(len(nums)):
        j = pivot + 2

        for i in range(1,len(nums)-1):
            j=i+1
            while (True):
                print('pivot : ' + str(pivot) + ', i : ' + str(i) + ', j : ' + str(j))
                # 여기에 구현
                if (nums[pivot] + nums[i] + nums[j] == 0):
                    temp = []
                    temp.append(nums[pivot])
                    temp.append(nums[i])
                    temp.append(nums[j])
                    result.append(temp)

                if j >= (len(nums) - 1):
                    break
                j += 1

        if i >= len(nums) - 2:
            break

    return result


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]

    result_for_print = sum_three_num_func(nums)

    print('result : ' + str(result_for_print))

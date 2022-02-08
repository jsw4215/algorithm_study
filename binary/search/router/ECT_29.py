from bisect import bisect_left, bisect_right


def solution(x, lst):

    lst.sort()


    def bin_search(nums):
        res = 0
        left = 0
        right = len(nums) - 1

        while left <= right:

            distance = (left + right) // 2

            installed = nums[0]
            cnt = 1

            for house in nums:

                if installed + distance <= house:
                    installed = house
                    cnt+=1

            if cnt >= x:
                left = distance + 1
                res = distance
            elif cnt < x:
                right = distance - 1

        return res

    result = bin_search(lst)

    return result

if __name__ == '__main__':

    x = 3
    lst = [1,2,8,4,9]

    result = solution(x, lst)

    print('result : ' + str(result))
from bisect import bisect_left, bisect_right


def solution(x, lst):






    def bin_search(nums):

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if mid > nums[mid]:
                left = mid + 1
            elif mid < nums[mid]:
                right = mid - 1
            else:
                return mid

        return -1

    result = bin_search(lst)

    return result

if __name__ == '__main__':

    x = 5
    lst = [-15, -6, 1, 3, 7]

    result = solution(x, lst)

    print('result : ' + str(result))
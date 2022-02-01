#binary DFS Templates
from binary.prac import make_tree_by


def solution(nums, target):

    left = 0
    right = len(nums)-1

    while left<=right:
        mid = (left + right) // 2

        if target>nums[mid]:
            left = mid+1
        elif target<nums[mid]:
            right = mid-1
        else:
            return mid

    return -1

if __name__ == '__main__':

    binTree = [-1,0,3,5,9,12]
    target = 9

    result = solution(binTree, target)

    print('result : ' + str(result))
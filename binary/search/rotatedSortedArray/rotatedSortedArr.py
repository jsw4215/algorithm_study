def solution(nums, target):

    if not nums:
        return False

    l = 0
    r = len(nums)-1

    while l < r :

        mid = (l+r)//2

        if nums[mid] == target :
            return True

        if nums[l] < nums[mid] :
            if nums[l]<=target<nums[mid]:
                r = mid
            else :
                l = mid+1

        elif nums[l] > nums[mid] :
            if nums[mid] < target <= nums[r]:
                l = mid+1
            else:
                r = mid
        else :
            l+=1

    return nums[l] == target


if __name__ == '__main__':

    nums = [4,5,6,7,0,1,2]
    target = 1

    result = solution(nums, target)

    print(str(result))
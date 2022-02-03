import sys

def solution(nums):

    def bi_search(num):

        left = 0
        right = len(temp)-1

        while left<=right:

            mid = (left + right)//2

            if num > temp[mid]:
                left = mid + 1
            elif num < temp[mid]:
                right = mid - 1
            else:
                return mid

    temp = []

    for i in nums:
        if not temp:
            temp.append(i)
        elif temp[-1] < i:
            temp.append(i)
        else:
            idx = bi_search(i)
            temp[idx] = i

    return len(temp)


n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

result = solution(nums)

print(str(result))
import heapq


def solution(n, m, k, nums):

    nums.sort(reverse=True)
    result=0
    first=nums.pop(0)
    i=0
    for _ in range(m):
       if i>=k:
            i=0
            result+=nums[0]
       else:
            result+=first
       i+=1

    print(f'{result}')


if __name__ == '__main__':

    n, m, k = 5, 8, 3
    nums = [2, 4, 5, 4, 6]

    solution(n, m, k, nums)

    # print(f'{l}')
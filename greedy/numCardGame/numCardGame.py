def solution(n, m, nums):
    temp_min=0
    min_i=-1
    for i in nums:
        temp = min(i)
        if temp_min<temp:
            temp_min=temp

    print(f'{temp_min}')


if __name__ == '__main__':

    n, m = 3, 3
    nums = [
        [3,1,2],
        [4,1,4],
        [2,2,2]
    ]

    solution(n, m, nums)

    # print(f'{l}')
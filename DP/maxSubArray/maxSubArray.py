nums = [-2,1,-3,4,-1,2,1,-5,4]

d = [0]*len(nums)

d[0] = -2
d[1] = 1

for i in range(2, len(nums)):
    if d[i-1] <= 0:
        d[i] = nums[i]
    else:
        d[i] = nums[i] + d[i-1]

print(f'{max(d)}')
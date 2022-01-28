from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    ans = []
    is_used = {i: False for i in range(-10, 11)}

    print('is_used : ' + str(is_used))

    def brute_force(index, current_list):
        # If, index is reached limit
        if index == len(nums):
            ans.append(current_list[:])
            return

        else:
            for i in nums:
                if is_used[i]:
                    continue
                else:
                    is_used[i] = True
                    current_list.append(i)
                    brute_force(index + 1, current_list)
                    is_used[i] = False
                    current_list.pop()

    brute_force(0, [])
    return ans

if __name__ == '__main__':

    inputNum = [1,2,3]

    result = permute(inputNum)

    print('result : ' + str(result))
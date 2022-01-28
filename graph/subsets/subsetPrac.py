def solution(inputNum):

    result = []
    prev_nodes = []
    next_nodes = []

    def dfs(nums):

        for i in range(len(nums)):
            next_nodes = nums[i:]
            next_nodes.remove(nums[i])

            prev_nodes.append(nums[i])
            result.append(prev_nodes[:])
            dfs(next_nodes)
            prev_nodes.pop()

    dfs(inputNum)

    #e를 제외한 subList와 비교하기

    result.append([])
    return result


if __name__ == '__main__':

    inputNum = [1,2,3]

    result = solution(inputNum)

    print('result : ' + str(result))
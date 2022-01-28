def solution(inputNum):

    result = []
    next_node = []
    prev_node = []



    def dfs(nums, index):

        result.append(nums)

        for i in range(index, len(inputNum)):
            dfs(nums + [inputNum[i]], i+1)


    dfs([],0)

    return result


if __name__ == '__main__':

    inputNum = [1,2,3]

    result = solution(inputNum)

    print('result : ' + str(result))
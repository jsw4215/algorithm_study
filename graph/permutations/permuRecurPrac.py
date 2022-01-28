def solution(inputNum):

    result = []
    next_nodes = []
    prev_nodes = []

    def dfsFunc(nums):
        if len(nums)==0:
            result.append(prev_nodes[:])


        for node in nums:
            next_nodes = nums[:]
            next_nodes.remove(node)

            prev_nodes.append(node)
            dfsFunc(next_nodes)
            prev_nodes.pop()

    dfsFunc(inputNum)

    return result




if __name__ == '__main__':

    inputNum = [1,2,3]

    result = solution(inputNum)

    print('result : ' + str(result))
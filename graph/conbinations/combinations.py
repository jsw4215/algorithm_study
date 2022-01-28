def solution(n, k):

    result = []

    nList = []

    curr_node = []
    next_node = []

    for i in range(1,n+1):
        nList.append(i)


    def dfsFunction(nList, k, index):
        k-=1
        if k<0:
            result.append(curr_node[:])
            return

        for i in range(index, len(nList)):
            next_node = nList[:]
            next_node.remove(nList[i])

            curr_node.append(nList[i])
            dfsFunction(next_node, k, index+1)
            curr_node.pop()

    dfsFunction(nList, k, 0)

    return result

if __name__ == '__main__':

    n = 4
    k = 2

    result = solution(n, k)

    print('result : ' + str(result))
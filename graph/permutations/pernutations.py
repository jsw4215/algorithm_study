def solution(inputNum):

    result = []
    prev_elements = []
    next_elements = []

    def dfs(elements):
        if len(elements) == 0:
            result.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(inputNum)

    return result


if __name__ == '__main__':

    inputNum = [1,2,3]

    result = solution(inputNum)

    print('result : ' + str(result))
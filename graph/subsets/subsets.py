def solution(inputNum):

    result = []
    prev_elements = []
    next_elements = []

    def dfs(elements):

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            prev_elements.sort()

            if prev_elements not in result:
                result.append(prev_elements[:])
            dfs(next_elements)
            elements.pop(0)
            prev_elements.pop()

    dfs(inputNum)

    return result


if __name__ == '__main__':

    inputNum = [1,2,3]

    result = solution(inputNum)

    print('result : ' + str(result))
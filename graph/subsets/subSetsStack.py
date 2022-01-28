import copy


def solution(inputNum):

    result = []
    visited = []
    stack = []

    stack = inputNum[:]



    while stack:

        for n in inputNum:
            stack = inputNum[:]
            visited.append(n)
            stack.remove(n)
            result.append(visited[:])
            for m in stack:
                visited.append(m)
                result.append(visited[:])

                for o in stack:
                    visited.append(o)
                    result.append(visited[:])
                    visited.pop()
                    visited.pop()

    return result


if __name__ == '__main__':

    inputNum = [1,2,3]

    result = solution(inputNum)

    print('result : ' + str(result))
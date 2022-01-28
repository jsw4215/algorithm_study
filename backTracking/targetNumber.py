def is_it_okay(vstd, target):
    tot = sum(vstd)

    if tot == target:
        return True
    else:
        return False


def solution(inputList, target):
    targetLen = len(inputList)
    visited = []
    result = []


    def dfs_stack(start, level):

       for node in range(start, targetLen):

            visited.append(inputList[node])

            if len(visited) != targetLen:
                dfs_stack(node+1, level+1)
                temp = visited.pop()
                visited.append(-temp)
                dfs_stack(node + 1, level + 1)
            else:
                if is_it_okay(visited, target):
                    result.append(visited[:])
                    visited.pop()
                    continue
            visited.pop()

       return

    dfs_stack(0,0)

    # if sum(inputList)==target:
    #     result.append(inputList)
    # temp = inputList.pop()
    # inputList.append(-temp)
    # if sum(inputList)==target:
    #     result.append(inputList)

    print(f'{result}')

    return len(result)


if __name__ == '__main__':

    # inputList = list(int(sys.stdin.readline()))
    # target = int(input())

    inputList = [1,1,1,1,1]
    target = 3

    result = []

    result.append(solution(inputList, target))

    print(str(result))
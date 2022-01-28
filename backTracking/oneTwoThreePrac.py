def is_it_okay(vstd):

    tot = sum(vstd)

    if tot == n:
        return True

    else:
        return False


def solution(n):
    result = []
    graph = [1,2,3]

    visited = []
    stack = []

    def dfs_stack(level, path):
        stack=[1,2,3]

        for adj in stack:
            visited.append(adj)
            if is_it_okay(visited) :
                result.append(visited[:])
                visited.pop()
                break
            else :
                dfs_stack(level+1,visited)
            visited.pop()

    dfs_stack(1,[])

    print('result : ' + str(result))

    return len(result)


if __name__ == '__main__':

    n=4

    result = []

    result.append(solution(n))

    print(str(result))
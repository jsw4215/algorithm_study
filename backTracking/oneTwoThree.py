def it_is_result(node, visited, n):

    visited.append(node)
    sumNodes = sum(visited)
    if sumNodes == n:
        return True
    elif sumNodes > n:
        return None

    return False


def solution(n):
    count = 0
    result = []
    graph = [1,2,3]

    visited = []
    stack = []

    def dfs_stack(start):

        for node in graph:
            checker = it_is_result(node, visited, n)
            if checker:
                result.append(visited[:])
                visited.pop()
                break
            if not checker:
                dfs_stack(start)
            visited.pop()
        return

    dfs_stack(1)

    return len(result)


if __name__ == '__main__':

    num = int(input())
    result = []

    for i in range(num):
        n = int(input())

        result.append(solution(n))

    for i in range(num):
        print(str(result[i]))
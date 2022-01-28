import collections


def solution(param, courses):

    graph = collections.defaultdict(list)

    for x,y in courses:
        graph[x].append(y)

    visited = set()

    def dfs(x):

        if x in visited:
            return False

        visited.add(x)
        for y in graph[x]:
            if not dfs(y):
                return False
        visited.remove(x)

        return True

    print(f'{graph}')
    print(f'{list(graph)}')
    print(f'{graph.keys()}')
    for x in list(graph):
        if not dfs(x):
            return False


    return True


if __name__ == '__main__':

    courses = [[0,1]]
    num = 3

    result = solution(3, courses)

    print(f'result : {result}')
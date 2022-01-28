import collections


def solution(param, courses):

    graph = collections.defaultdict(list)

    for x,y in courses:
        graph[x].append(y)

    visited = set()

    def dfs(key):

        if key in visited:
            return False

        visited.add(key)
        for value in graph[key]:
            if not dfs(value):
                return False

        #각 key별로 depth 타고들어갔다가 나올 때 visited를 깨끗하게 비워주기 위함
        visited.remove(key)

        return True

    for start in list(graph):
        #visited.clear()
        if not dfs(start):
            return False

    return True


if __name__ == '__main__':

    courses = [[1,4],[2,4],[3,1],[3,2]]
    num = 3

    result = solution(3, courses)

    print(f'result : {result}')
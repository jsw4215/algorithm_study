from typing import List
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()

        def dfs(i):
            if i in traced:
                return False

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)


            return True


        for x in list(graph):
            if not dfs(x):
                return False


        return True


if __name__ == '__main__':

    courses = [[0,1],[1,0]]
    num = 3

    sol = Solution()

    result = sol.canFinish(3, courses)

    print(f'result : {result}')
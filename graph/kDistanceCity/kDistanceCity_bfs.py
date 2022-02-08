import collections
import sys


def solution(start, k, lst):

    result = []
    visited = [-1]*(n+1)

    def bfs_queue(start, visited, lv):
        visited[start] = lv
        q = collections.deque([start])

        while q:
            temp = q.popleft()
            lv = visited[temp]
            lv += 1
            for node in path[temp]:

                if visited[node]==-1:
                    visited[node] = lv
                    q.append(node)

        return visited


    bfs_queue(start, visited, 0)
    checker=0
    for i in range(len(visited)):
        if visited[i] == k:
            checker+=1
            print(i)

    if not checker:
        print(-1)

    pass


if __name__ == '__main__':

    input = sys.stdin.readline

    n, numOfWay, kDistance, startingPoint = map(int, input().split())

    path = [[] for _ in range(n + 1)]
    for _ in range(numOfWay):
        a, b = map(int, input().split())
        path[a].append(b)

    solution(startingPoint, kDistance, path)

# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4
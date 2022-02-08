import collections
import sys


def solution(start, k, lst):

    result = []
    dict = collections.defaultdict(list)
    visited = [-1]*(n+1)


    #lst dict형태로 변환
    for i in lst:
        if dict[i[0]] is None:
            dict[i[0]] = [i[1]]
        else:
            dict[i[0]].append(i[1])

    def dfs_recursive(node, distance,lv):

        # 방문처리
        if distance[node] == -1:
            distance[node] = lv
        elif distance[node] > lv:
            distance[node] = lv

        if len(dict[node])==0:
            return
        if lv == k:
            return

        # 인접 노드 방문
        for adj in dict[node]:
            dfs_recursive(adj, distance, lv+1)

        return

    cnt = 0
    dfs_recursive(start, visited, 0)

    checker = 0
    for i in range(len(visited)):
        if visited[i] == k:
            checker += 1
            print(i)

    if not checker:
        print(-1)

    pass


if __name__ == '__main__':

    input = sys.stdin.readline

    n, numOfWay, kDistance, startingPoint = map(int, input().split())
    ways = []

    for _ in range(numOfWay):
        temp = list(map(int, input().split()))
        ways.append(temp)

    solution(startingPoint, kDistance, ways)

import collections
import sys

def bfs_queue(start):

    q = collections.deque([start])
    visited = [False]*(n+1)
    cost = [0]*(n+1)
    arr = []
    visited[x] = True
    while q:
        now = q.popleft()
        newCost = cost[now]+1

        for node in graph[now]:
            if newCost>k:
                continue
            if not visited[node]:
                visited[node] = True
                cost[node] = newCost
                if cost[node] == k:
                    arr.append(node)
                    continue
                q.append(node)
                visited.append(node)

    return arr

def solution():

    res = bfs_queue(x)

    return res

if __name__ == '__main__':
    
    input = sys.stdin.readline

    n, m, k, x = map(int, sys.stdin.readline().split())

    legs = []

    for _ in range(m):
        temp = list(map(int, sys.stdin.readline().split()))
        legs.append(temp)

    graph = collections.defaultdict(list)

    for i,j in legs:
        graph[i].append(j)

    res = solution()

    if len(res)==0:
        print(-1)
    else:
        res.sort()
        for item in res:
            print(item)
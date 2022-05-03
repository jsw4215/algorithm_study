import collections
import sys

def getFalseNode():
    for i in range(visited):
        if not visited[i]:
            return i
    return -1

def isFinish():
    for item in visited:
        if not item:
            return False
    return True

def getEdge(graph):
    
    cnt=0
    nextNode = 1

    q = collections.deque([1])

    while True:

        nextNode = q.popleft()

        if graph[nextNode] is None:
            cnt+=1
            if isFinish():
                break

        if visited[nextNode]:
            nextNode = getFalseNode()
            cnt+=2
            if isFinish():
                break
        else:
            visited[nextNode] = True

        q.extend(graph[nextNode])


    
    return cnt

def solution():
    
    graph = collections.defaultdict(list)

    visited[0] = True

    for key, value in arr:
        graph[key].append(value)
        graph[value].append(key)

    res = getEdge(graph)

    return res-1

if __name__ == '__main__':
    
    input = sys.stdin.readline

    n, m = map(int, input().split())

    arr = []

    for _ in range(0, m):
        temp = list(map(int, sys.stdin.readline().split()))
        arr.append(temp)
    
    visited = [False]*(n+1)

    res = solution()

    print(res)

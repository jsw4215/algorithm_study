#binary BFS Templates
import sys
import collections

def solution(n, nodes, target):
    if nodes[target]==-1:
        return 0

    graph = collections.defaultdict(list)

    for i in range(n):
        if nodes[i] != -1:
            graph[nodes[i]].append(i)
            graph[i].append(nodes[i])

    def defTargetDel(_target):

        if _target is None:
            return

        temp = graph[_target]
        graph.pop(_target)

        for i in temp:
            defTargetDel(i)


    graph[nodes[target]].remove(target)
    graph[target].remove(nodes[target])

    defTargetDel(target)

    if len(graph) == 1:
        return 1

    result=0

    for i in graph:
        if len(graph[i])==1:
            #부모노드 아닌것 확인
            if nodes[i]==-1:
                continue
            result+=1

    return result

if __name__ == '__main__':

    n = int(sys.stdin.readline())
    nodes = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())

    result = solution(n, nodes, target)

    print(f'{result}')
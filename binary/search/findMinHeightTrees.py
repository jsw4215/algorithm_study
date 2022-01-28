#binary BFS Templates
import collections
from collections import deque

from binary.prac import make_tree_by


def solution(n, edges):

    graph = collections.defaultdict(list)

    for i,j in edges:
        graph[i].append(j)
        graph[j].append(i)

    print(f'{graph}')

    leaf = []

    for i in range(n+1):
        if len(graph[i]) == 1:
            leaf.append(i)

    while n>2:
        n -= len(leaf)
        temp_leaf = []

        for i in leaf:
            temp=graph[i].pop()
            graph[temp].remove(i)

            if(len(graph[temp])==1):
                    temp_leaf.append(temp)

        leaf = temp_leaf

    return leaf

if __name__ == '__main__':

    n =6

    edges = [[0,3],[1,3],[2,3],[4,3],[5,4]]

    result = solution(n, edges)

    print(f'{result}')
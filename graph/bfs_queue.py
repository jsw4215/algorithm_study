from collections import deque

from graph.dfs_bfs.prac import graph


def bfs_queue(start):
    visited = [start]
    q = deque([start])

    while q:
        temp = q.popleft()

        for node in graph[temp]:
            if node not in visited:
                visited.append(node)
                q.append(node)

    return visited


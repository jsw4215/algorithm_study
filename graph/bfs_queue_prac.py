from collections import deque

from graph.dfs_bfs.prac import graph


def bfs_queue(start):

    visited = [start]
    q = deque([start])

    while q:
        node = q.popleft()

        for node in graph[node]:
            if node not in visited:
                q.append(node)
                visited.append(node)

    return visited


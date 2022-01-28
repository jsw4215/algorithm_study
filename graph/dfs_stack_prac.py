from graph.dfs_bfs.prac import graph


def dfs_stack(start):
    stack = [start]
    visited = []

    while stack:
        top = stack.pop()
        visited.append(top)

        for adj in graph[top]:
            if adj not in visited:
                stack.append(adj)

    return visited

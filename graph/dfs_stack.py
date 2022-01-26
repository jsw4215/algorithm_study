def dfs_stack(start):
    visited = []
    stack = [start]

    while stack:
        top = stack.pop()
        visited.append(top)

        for adj in graph[top]:
            if adj not in visited:
                stack.append(adj)

    return visited
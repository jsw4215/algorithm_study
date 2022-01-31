from collections import deque


def dfs_stack(start, graph):
    stack = [start]
    visited = []

    while stack:
        top = stack.pop()
        visited.append(top)

        for adj in graph[top]:
            if adj not in visited:
                stack.append(adj)

    return visited


def dfs_recursive(start, visited):

    visited.append(start)

    for adj in graph[start]:
        if adj not in visited:
            dfs_recursive(adj, visited)

    return visited

def bfs_queue(start):

    queue = deque([start])
    visited = [start]

    while queue:
        temp = queue.popleft()


        for adj in graph[temp]:
            if adj not in visited:
                queue.append(adj)
                visited.append(adj)

    return visited



if __name__ == '__main__':

    l = []

    graph = {
        1: [2, 3, 4],
        2: [5],
        3: [5],
        4: [],
        5: [6, 7],
        6: [],
        7: [3],
    }

    test = bfs_queue(1)

    print(f'result: {test}')
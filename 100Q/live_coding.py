from collections import deque

graph = {
    1:[2,3],
    2:[4,5],
    3:[],
    4:[],
    5:[]
}

def bfs(start):

    queue = deque([start])
    visited = [start]

    while queue:
        temp = queue.popleft()

        for adj in graph[temp]:
            if adj not in visited:
                queue.append(adj)
                visited.append(adj)

    return visited

result = bfs(1)

print(f'{result}')

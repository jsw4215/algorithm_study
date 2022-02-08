import collections
import heapq
from typing import List


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = collections.defaultdict(dict)
    heap = [(0, src, k + 1)]
    visits = [0] * n

    for start, togo, cost in flights:
        graph[start][togo] = cost

    while heap:
        cost, start, togo = heapq.heappop(heap)

        if start == dst:
            return cost

        if visits[start] >= togo:
            continue

        visits[start] = togo

        for new_end, new_cost in graph[start].items():
            heapq.heappush(heap, (cost + new_cost, new_end, togo - 1))

    return -1

if __name__ == '__main__':

    n = 5
    src = 0
    dst = 4
    k = 3

    times = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1],[3, 4, 1]]

    result = findCheapestPrice(n, times, src, dst, k)

    print(f'{result}')
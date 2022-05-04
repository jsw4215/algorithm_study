from collections import defaultdict
import heapq
from typing import List

INF = float('inf')


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    adj = defaultdict(dict)
    for f, t, p in flights:
        adj[f][t] = p
    print(adj)
    stop = [INF] * n
    heap = [(0, 0, src)]

    while heap:
        current_price, current_stop, current_node = heapq.heappop(heap)

        if current_node == dst:
            return current_price
        if current_stop == k + 1 or current_stop >= stop[current_node]:
            continue

        stop[current_node] = current_stop

        for c, p in adj[current_node].items():
            heapq.heappush(heap, (current_price + p, current_stop + 1, c))

    return -1



if __name__ == '__main__':

    n = 5
    src = 0
    dst = 4
    k = 3

    times = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1],[3, 4, 1]]

    result = findCheapestPrice(n, times, src, dst, k)

    print(f'{result}')
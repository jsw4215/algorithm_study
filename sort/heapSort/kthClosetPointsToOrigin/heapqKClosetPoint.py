import heapq
import math


def cal_dist(point):
    return math.sqrt(point[0] * point[0] + point[1] * point[1])

def k_closest_builtin(points, k):
    dists = []
    heap = []
    for point in points:
        dist = cal_dist(point)
        heapq.heappush(heap, dist)
        dists.append(dist)

    kth_dist = [heapq.heappop(heap) for _ in range(k)][-1]
    return [points[idx] for idx, dist in enumerate(dists) if dist <= kth_dist]
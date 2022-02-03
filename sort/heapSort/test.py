import math

from heap.max.structures import BinaryMaxHeap

def cal_dist(point):
    return math.sqrt(point[0] * point[0] + point[1] * point[1])

def sorted_by_heap(lst):
    maxheap = BinaryMaxHeap()
    for elem in lst:
        maxheap.insert(elem)

    desc = [maxheap.extract() for _ in range(len(lst))]
    return list(reversed(desc))
import heapq
import sys

if __name__ == '__main__':

    number = int(input())
    heap = []

    for i in range(number):
        num = int(sys.stdin.readline())
        if num==0:
            try:
                temp = heapq.heappop(heap)
                print(temp)
            except:
                print('0')
        else:
            heapq.heappush(heap, num)
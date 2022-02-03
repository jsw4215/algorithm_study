import heapq


def solution(scoville, k):

    if len(scoville)==1 or scoville is None:
        return 0

    heapq.heapify(scoville)
    cnt = 0

    while True:
        try:
            cnt+=1
            lowest1 = heapq.heappop(scoville)
            lowest2 = heapq.heappop(scoville)

            newScoville = lowest1 + (lowest2*2)

            heapq.heappush(scoville, newScoville)

            if scoville[0] >= k:
                break
        except IndexError:
            cnt = -1
            break

    return cnt

if __name__ == '__main__':

    scoville = [1, 2, 3, 9, 10, 12]
    k = 7

    result = solution(scoville, k)

    print(f'{result}')

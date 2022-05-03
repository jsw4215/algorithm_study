import heapq
from typing import List

def solution(food_times: List[int], k: int):
    # 음식을 다 먹어서 더 먹을 게 없는 경우
    if sum(food_times) <= k:
        return -1

    # 힙 (최소힙) 자료구조를 사용
    # 힙에 (음식시간, 음식번호)를 넣습니다. 음식시간 기준으로 최소힙 정렬이 됩니다.
    h = []
    for i, food_time in enumerate(food_times):
        heapq.heappush(h, (food_time, i + 1))

    # 음식 먹은 총 시간
    total_elapsed_time = 0

    # 현재까지 각 음식을 먹는 데 걸린 최대시간
    # 예를들어 food_times: [1,3,5,9]이고 현재 5까지 진행됐으면 5입니다
    each_eating_time = 0

    length = len(h)  # 음식 개수
    # 최소 음식시간 * 남은 음식들 개수 < 음식을 먹을 수 있는 시간  (현재 음식을 다 먹을 수 있는 조건이 만족됩니다)
    while length * (h[0][0] - each_eating_time) < (k - total_elapsed_time):
        total_elapsed_time += length * (h[0][0] - each_eating_time)
        each_eating_time += (h[0][0] - each_eating_time)
        print("h,before",h)
        heapq.heappop(h)
        print("h,after",h)
        length -= 1

    # 음식 번호 순으로 정렬하고
    # mod 연산을 이용해서 먹을 음식을 구합니다
    result = sorted(h, key=lambda x: x[1])
    return result[(k - total_elapsed_time) % len(h)][1]


res = solution([3,1,2],5)
print("res",res)
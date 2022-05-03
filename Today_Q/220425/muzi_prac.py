import heapq

def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    tot_time = 0
    cycle = 0
    h=[]

    for i, food_times in enumerate(food_times):
        heapq.heappush(h, (food_times, i+1))

    print("h",h)

    num_foods = len(h)

    while k > tot_time + ((h[0][0] - cycle) * num_foods):
        
        tot_time += (h[0][0] - cycle) * num_foods
        cycle += (h[0][0] - cycle)
        print("tot!", tot_time)
        heapq.heappop(h)
        num_foods-=1

    remain = sorted(h, key=lambda x: x[1])
    print("remain", k - tot_time, remain)
    return remain[(k - tot_time) % num_foods][1]     
    
if __name__ == '__main__':

    l = [3,1,2]
    n = 5

    res = solution(l,n)

    print("res",res)
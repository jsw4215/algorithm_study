def solution(food_times, k):
    if k >= sum(food_times):
        return -1
    sorted_times = sorted(enumerate(food_times), key=lambda x: x[1])
    length = len(food_times)
    standard = 0
    for idx in range(length):
        k -= (length-idx)*(sorted_times[idx][1]-standard)
        if k <= 0:
            return sorted(sorted_times[idx:], key=lambda x: x[0])[k % (length-idx)][0]+1
        standard = sorted_times[idx][1]
    
if __name__ == '__main__':

    l = [3,1,2]
    n = 5

    res = solution(l,n)

    print("res",res)
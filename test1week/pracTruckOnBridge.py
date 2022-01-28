from collections import deque


def solution(bridge_length, weight, truck_weights):
    tot=0
    bride_status=deque([0]*bridge_length)

    while(bride_status):
        tot+=1
        bride_status.popleft()

        if truck_weights:
            if sum(bride_status) + truck_weights[0] <= weight:
                bride_status.append(truck_weights.popleft())
            else:
                bride_status.append(0)


    return tot


if __name__ == '__main__':

    bridge_length = 2
    weight = 10
    truck_weights = deque([7,4,5,6])

    result = solution(bridge_length, weight, truck_weights)

    print('result : ' + str(result))
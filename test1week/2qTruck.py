def solution(bridge_length, weight, truck_weights):
    #큐에 순서대로 넣고
    #length만큼 있는다.
    #단, 무게비교시 트럭이 더 올라갈 수 있으면, 올라간다.
    bridge_queue = [0]*bridge_length
    tot=0

    while(bridge_queue):
        tot+=1
        bridge_queue.pop(0)
        if truck_weights:
            if sum(bridge_queue) + truck_weights[0]<=weight:
                temp = truck_weights.pop(0)
                bridge_queue.append(temp)
            else:
                bridge_queue.append(0)

    return tot


if __name__ == '__main__':

    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10]

    result = solution(bridge_length, weight, truck_weights)

    print('result : ' + str(result))
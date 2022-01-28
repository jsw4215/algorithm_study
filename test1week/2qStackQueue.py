def solution(bridge_length, weight, truck_weights):
    #큐에 순서대로 넣고
    #length만큼 있는다.
    #단, 무게비교시 트럭이 더 올라갈 수 있으면, 올라간다.
    bridge_queue = []
    term_per_truck = []
    tot=0

    for t, truck in enumerate(truck_weights):
        #트럭 올리고 타이머 올리고
        bridge_queue.append(truck)
        term_per_truck.append(0)

        while(term_per_truck[-1]<=bridge_length):
            tot += 1
            #타이머 +1
            for i in range(len(term_per_truck)):
                term_per_truck[i]+=1

            print('term per truck : ' + str(term_per_truck))

            sum_trucks_on_bridge = sum(bridge_queue)
            print('sum trucks on bridge : ' + str(sum_trucks_on_bridge))

            if term_per_truck[0] >= bridge_length:
                bridge_queue.pop(0)
                term_per_truck.pop(0)

            #트럭한대 더 올림
            if t!= len(truck_weights)-1:
                if truck_weights[t+1] + truck <= weight or len(bridge_queue) == 0:
                    break
            elif len(bridge_queue)==0:
                tot+=1
                break
            print('tot : ' + str(tot))


    return tot


if __name__ == '__main__':

    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10]

    result = solution(bridge_length, weight, truck_weights)

    print('result : ' + str(result))
from bisect import bisect_left, bisect_right
from collections import deque

def findOrder(dicList):
    dicList = deque(dicList)
    order = [dicList.popleft()[0]]
    for i in range(len(dicList)):
        x = dicList[i][0]
        
        left = bisect_left(order, x)
        #이미 있는 경우
        if left<len(order):
            continue
        #없는 경우
        right = bisect_right(order, x)
        order.append(dicList[i][0])
    
    for i in range(len(dicList)):
        dicList[i] = dicList[1:]

    findOrder

    return order





def solution(lst):



    res = findOrder(lst)

    return res

if __name__ == '__main__':

    lst = ["xz","xy","z"]

    result = solution(lst)

    print('result : ' + str(result))